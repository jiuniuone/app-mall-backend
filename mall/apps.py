from django.apps import AppConfig as DjangoAppConfig

CREATE_MENU_ENABLED = True


class AppConfig(DjangoAppConfig):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = 'mall'

    def ready(self):
        from mall.signals import app_ready
        app_ready.send(self.__class__)
