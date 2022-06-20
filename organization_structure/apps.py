from django.apps import AppConfig


class OrganizationStructureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'organization_structure'

    def ready(self):
        import organization_structure.signals
