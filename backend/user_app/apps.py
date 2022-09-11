from django.apps import AppConfig


class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_app'

    # TODO: Uncomment this after signals has been created:
    def ready(self):
        import user_app.signals
