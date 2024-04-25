# Librairie EPSIC

Web app simple écrite avec Django pour le module 450.

## Installation des dépendances

1. Web framework Django :
   ```
   pip install Django
   ```
2. Test framework :
   ```
   pip install pytest-django
   ```

## Mise à jour de la DB

1. Pour créer la BD selon les modèles crées:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Pour créer un superuser : 
   ```
   python manage.py createsuperuser
   ```

## Exécution
1. Exécuter l'app :
   ```
   python3 manage.py runserver
   ```
2. Consulter l'app @ `http://127.0.0.1:8000`
3. Exécuter les tests :
   ```
   pytest -v
   ```

