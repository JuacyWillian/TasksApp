# coding= utf-8
from enum import Enum

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemeManager

from tasks.models import db, table_list
from tasks.screens import SCREENS_TYPE, SCREEN_LIST
from tasks.screens.home_screen import HomeScreen


class TasksApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    logo = StringProperty(u'assets/image/logo.png')
    version = StringProperty('')
    description = StringProperty('')
    developers = ListProperty([])
    website = StringProperty('')

    def __init__(self, **kwargs):
        super(TasksApp, self).__init__(**kwargs)
        with db:
            db.create_tables(table_list)

        self.logo = u'assets/image/logo.png'
        self.description = u'''Tasks é um aplicativo simples que ajuda o usuário a organizar o seu dia-a-dia listando as tarefas a serem realizadas e as que já foram completadas.

        O aplicativo foi construido usando Python como linguagem de programação, Kivy como Framework GUI multiplataforma, KivyMD como tema de acordo com os padrões do Material Design do Google e Peewee para facilitar o acesso ao banco de dados SQLite.'''
        self.version = u'0.01'
        self.developers = [
            (u'Juacy Willian', u'http://twitter.com/juacywillian'),
        ]
        self.website = u'http://juacywillian.github.io/tasks'

    def build(self):
        self.goto(SCREENS_TYPE.HOME)
        return self.root

    def goto(self, screenType, **kwargs):
        if not isinstance(screenType, Enum):
            raise TypeError(
                u"'screenType' param  must be a 'SCREEN_TYPE' instance.")

        screen = SCREEN_LIST[screenType](**kwargs)
        self.root.ids.manager.switch_to(screen)
