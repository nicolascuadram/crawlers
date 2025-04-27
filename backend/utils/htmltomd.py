from bs4 import BeautifulSoup

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
