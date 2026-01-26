from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = 'test_app'

    def get_model(self, model_name, require_ready=True):
        return
