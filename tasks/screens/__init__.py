from kivy.uix.screenmanager import Screen


class BaseScreen(Screen):
    def on_pre_enter(self, *args):
        super().on_pre_enter(*args)

    def on_enter(self, *args):
        super().on_enter(*args)

    def on_pre_leave(self, *args):
        super().on_pre_leave(*args)

    def on_leave(self, *args):
        super().on_leave(*args)


from .splash_screen import SplashScreen
from .home_screen import HomeScreen
from .task_edit_screen import TaskEditScreen
