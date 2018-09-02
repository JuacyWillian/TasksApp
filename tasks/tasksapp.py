from kivy.app import App
from kivymd.theming import ThemeManager

from tasks.models import db, table_list


class TasksApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def __init__(self, **kwargs):
        super(TasksApp, self).__init__(**kwargs)
        with db.connection():
            db.create_tables(table_list)

    def build(self):
        return self.root


tasks_app = TasksApp()
