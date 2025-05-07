import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lojaonline.settings')  # ajuste para o nome do seu projeto
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
password = 'admin123'
email = 'admin@example.com'

if not User.objects.filter(username=username).exists():
    print("Criando superusuário...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("Superusuário já existe.")
