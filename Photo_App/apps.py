from django.apps import AppConfig


class PhotoAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Photo_App"

    def ready(self):
        import Photo_App.signals