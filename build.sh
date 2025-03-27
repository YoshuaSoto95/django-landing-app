set -o errexit

#!/bin/bash

# Instalar las dependencias de Python
# pip install -r requirements.txt

# Aplicar migraciones
python manage.py migrate

# Crear superusuario automáticamente (si no existe)
python manage.py shell <<EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@admin.com', 'password123')
EOF

# Recopilar archivos estáticos
python manage.py collectstatic --noinput

# Iniciar el servidor
# gunicorn manage_landing.wsgi:application --bind 0.0.0.0:8000
