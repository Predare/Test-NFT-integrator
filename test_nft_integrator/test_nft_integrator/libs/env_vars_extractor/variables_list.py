from dotenv import dotenv_values

config = dotenv_values(".env")

django_secret_key = config['DJANGO_SECRET_KEY']