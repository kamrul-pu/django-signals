from django.apps import AppConfig


class SignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals'

    #Add function for writing signals on different files
    def ready(self):
        #signals app name
        import signals.mysignals
