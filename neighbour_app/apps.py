from django.apps import AppConfig


class NeighbourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'neighbour_app'

    def ready(self):
        import neighbour_app.signals
