set -o errexit

#!/bin/bash

# Instalar las dependencias de Python
# pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Recopilar archivos estáticos
python manage.py collectstatic --noinput

# Iniciar el servidor
# gunicorn manage_landing.wsgi:application --bind 0.0.0.0:8000
