if __name__ == "__main__":
    import os
    import django

    # Configure the DJANGO_SETTINGS_MODULE environment variable
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    # Initialize Django
    django.setup()

    from dictionary.models import DiplomaticTerm
    import orjson

    file = open('result.json', 'r')
    data: dict = orjson.loads(file.read())
    DiplomaticTerm.objects.bulk_create([DiplomaticTerm(title=k, definition=v) for k, v in data.items()], batch_size=100)
    file.close()
