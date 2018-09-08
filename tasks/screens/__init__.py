from enum import Enum
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.navigationdrawer import NavigationLayout

SCREENS_TYPE = Enum('Screens', 'HOME EDIT ABOUT')


class BaseScreen(Screen):
    app = ObjectProperty(None)
    toolbar = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self, *args):
        super(BaseScreen, self).on_pre_enter(*args)

    def on_enter(self, *args):
        super(BaseScreen, self).on_enter(*args)

    def on_pre_leave(self, *args):
        super(BaseScreen, self).on_pre_leave(*args)

    def on_leave(self, *args):
        super(BaseScreen, self).on_leave(*args)


from tasks.screens.about_screen import AboutScreen
from tasks.screens.home_screen import HomeScreen
from tasks.screens.task_edit_screen import TaskEditScreen

SCREEN_LIST = {
    SCREENS_TYPE.HOME: HomeScreen,
    SCREENS_TYPE.EDIT: TaskEditScreen,
    SCREENS_TYPE.ABOUT: AboutScreen
}
