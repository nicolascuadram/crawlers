#!/bin/bash

# Ruta absoluta al proyecto ()
PROJECT_DIR="~/crawlers"
BACKEND_DIR="$PROJECT_DIR/backend"
VENV_DIR="$BACKEND_DIR/venv"

# Entrar al directorio del proyecto
cd "$PROJECT_DIR"

# Activar entorno virtual
if [ ! -d "$VENV_DIR" ]; then
    echo "⚙️  Creando entorno virtual en $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
fi

echo "✅ Activando entorno virtual..."
source "$VENV_DIR/bin/activate"

# Instalar dependencias si es necesario
#echo "📦 Instalando dependencias..."
#pip install --upgrade pip
#pip install -r "$PROJECT_DIR/backend/requirements.txt"

echo "🚀 Ejecutando crawler..."
python3 "$PROJECT_DIR/backend/crawler.py"

echo "📝 Ejecutando writer..."
python3 "$PROJECT_DIR/backend/writer.py"

echo "📤 Haciendo commit y push de frontend..."
cd "$PROJECT_DIR/frontend"
git add .
git commit -m "log [scraping $(date '+%Y-%m-%d %H:%M:%S')]"
git push

echo "✅ Proceso finalizado: $(date)"
