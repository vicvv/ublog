from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

   #  needed to create profile at the same as user
    def ready(self):
        import users.signals
