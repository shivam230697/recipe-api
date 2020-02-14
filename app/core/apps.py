from django.apps import AppConfig


class CoreConfig(AppConfig):

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)

    name = 'core'
