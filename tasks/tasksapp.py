from datetime import date, datetime

from kivy.app import App
from kivy.core.window import Window
from kivy.properties import *
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivymd.label import MDLabel
from kivymd.list import (ILeftBody, IRightBodyTouch, MDList, OneLineListItem,
                         TwoLineIconListItem)
from kivymd.navigationdrawer import NavigationDrawerHeaderBase
from kivymd.theming import ThemableBehavior, ThemeManager

from tasks.models import Person, Task, db
from tasks.screens import *


class TasksApp(App):
    """Basic kivy app

    Edit tasks.kv to get started.
    """
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        self.db = db

        return self.root

    def on_request_close(self, *args):
        # print('request close')
        # return True
        pass

    def on_stop(self, ):
        print('on stop')

    def get_widget(self, id):
        return root.ids[id]
