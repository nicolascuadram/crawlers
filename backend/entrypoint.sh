#!/bin/bash

echo "Esperando a que la base de datos esté disponible..."

sleep 10

echo "Ejecutando los scripts por primera vez..."

python /app/crawler.py && python /app/writer.py


# Agregar tarea cron al archivo crontab
echo "0 */4 * * * python /app/crawler.py && python /app/writer.py >> /var/log/cron.log 2>&1" > /etc/cron.d/scraper-job

chmod 0644 /etc/cron.d/scraper-job
crontab /etc/cron.d/scraper-job

touch /var/log/cron.log

cron && tail -f /var/log/cron.log
