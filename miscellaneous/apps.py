from django.apps import AppConfig


class MiscellaneousConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'miscellaneous'

    def ready(self):
        import miscellaneous.signals