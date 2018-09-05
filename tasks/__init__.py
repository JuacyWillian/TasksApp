from kivy.app import App
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationLayout

from tasks.models import db, table_list
from tasks.screens import HomeScreen


class TasksApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def __init__(self, **kwargs):
        super(TasksApp, self).__init__(**kwargs)
        with db.connection():
            db.create_tables(table_list)

    def build(self):

        self.root.ids.manager.switch_to(HomeScreen(name='home'))
        return self.root
