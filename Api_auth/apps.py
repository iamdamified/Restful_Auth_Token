from django.apps import AppConfig


class ApiAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Api_auth'

    def ready(self):
        import Api_auth.signals
