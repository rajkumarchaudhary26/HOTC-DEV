from django.apps import AppConfig


class BoardMembersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board_members'
    
    def ready(self):
        import board_members.signals
