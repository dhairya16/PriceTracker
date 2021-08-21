from django.apps import AppConfig


class LinksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'links'

    def ready(self):
        from jobs import updater
        updater.start()
