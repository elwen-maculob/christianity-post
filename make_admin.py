import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'christianity_post.settings')
django.setup()

print("Connected to database:", connection.settings_dict['NAME'])

from django.contrib.auth.models import User
if not User.objects.filter(username='CP_Elwen').exists():
    User.objects.create_superuser('CP_Elwen', 'elwenmaculob.em@gmail.com', 'Elwen1234')
    print("Superuser created!")
else:
    print("User already exists in this database!")