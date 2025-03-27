from django.contrib.auth.models import User

# Verificar si ya existe un superusuario con ese nombre
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('yoshua', 'yoshuasoto55@gmail.com', 'mibandaes12')

    