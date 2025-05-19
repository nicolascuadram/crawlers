from bs4 import BeautifulSoup
from selectolax.parser import HTMLParser

def html_to_markdown(soup_element):
    markdown = ""
    
    for elem in soup_element.descendants:
        if elem.name:
            if elem.name.startswith('h') and elem.name[1].isdigit():
                # Encabezados h1, h2, h3...
                level = int(elem.name[1])
                text = elem.get_text(strip=True)
                markdown += f"\n{'#' * level} {text}\n\n"
            elif elem.name == 'p':
                # Párrafos
                text = elem.get_text(strip=True)
                if text:
                    markdown += f"{text}\n\n"
            elif elem.name == 'pre':
                # Bloques de código
                code_text = elem.get_text(strip=True)
                markdown += f"\n```shell\n{code_text}\n```\n\n"
            elif elem.name == 'code' and elem.parent.name != 'pre':
                # Código en línea
                code_inline = elem.get_text(strip=True)
                markdown += f"`{code_inline}`"
            elif elem.name == 'ul':
                pass
            elif elem.name == 'ol':
                pass
            elif elem.name == 'li':
                # Items de listas
                parent = elem.find_parent()
                text = elem.get_text(strip=True)
                if parent.name == 'ul':
                    markdown += f"- {text}\n"
                elif parent.name == 'ol':
                    markdown += f"1. {text}\n"
            elif elem.name == 'img':
                # Imagenes
                alt = elem.get('alt', 'Image')
                src = elem.get('src')
                if src:
                    markdown += f"\n![{alt}]({src})\n\n"
        elif elem.string:
            text = elem.string.strip()
            if text:
                markdown += f"{text} "
    
    # limpiar espacios duplicados
    return '\n'.join(line.strip() for line in markdown.splitlines() if line.strip())

def html_to_markdown_selectolax(node):
    from selectolax.parser import HTMLParser
    if hasattr(node, 'root'):
        node = node.root  # Asegura que tienes el nodo raíz

    if node is None:
        return ''

    def iter_children(node):
        child = node.child  # Aquí es child, no first_child
        while child:
            yield child
            child = child.next

    def convert(node):
        if node.tag == 'p':
            return convert_children(node).strip() + '\n\n'
        elif node.tag in ('b', 'strong'):
            return f"**{convert_children(node)}**"
        elif node.tag in ('i', 'em'):
            return f"*{convert_children(node)}*"
        elif node.tag == 'a':
            href = node.attributes.get('href', '#')
            return f"[{convert_children(node)}]({href})"
        elif node.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(node.tag[1])
            return f"{'#' * level} {convert_children(node)}\n\n"
        elif node.tag == 'ul':
            return '\n'.join(f"- {convert(child)}" for child in iter_children(node) if child.tag == 'li') + '\n\n'
        elif node.tag == 'ol':
            return '\n'.join(f"{i+1}. {convert(child)}" for i, child in enumerate(iter_children(node)) if child.tag == 'li') + '\n\n'
        elif node.tag == 'li':
            return convert_children(node)
        elif node.tag == 'br':
            return '\n'
        elif node.tag is None:
            return node.text() or ''
        else:
            return convert_children(node)

    def convert_children(parent):
        return ''.join(convert(child) for child in iter_children(parent))

    return convert(node).strip()

