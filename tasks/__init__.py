from enum import Enum
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import *
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationLayout

from tasks.models import db, table_list
from tasks.screens import SCREENS_TYPE, SCREEN_LIST
from tasks.screens.home_screen import HomeScreen


class TasksApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    logo = StringProperty('data/image/logo.png')
    version = StringProperty('')
    description = StringProperty('')
    developers = ListProperty([])
    website = StringProperty('')

    def __init__(self, **kwargs):
        super(TasksApp, self).__init__(**kwargs)
        with db.connection():
            db.create_tables(table_list)

        self.logo = 'data/image/logo.png'
        self.description = '''Mussum Ipsum, cacilds vidis litro abertis. Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis. Manduma pindureta quium dia nois paga. In elementis mé pra quem é amistosis quis leo. Copo furadis é disculpa de bebadis, arcu quam euismod magna.

Mé faiz elementum girarzis, nisi eros vermeio. Em pé sem cair, deitado sem dormir, sentado sem cochilar e fazendo pose. Detraxit consequat et quo num tendi nada. Delegadis gente finis, bibendum egestas augue arcu ut est. '''
        self.version = '0.01'
        self.developers = []
        self.website = 'http://juacywillian.github.io/tasks'

    def build(self):
        # self.root.ids.manager.transition = RiseInTransition()
        self.goto(SCREENS_TYPE.HOME)
        return self.root

    def goto(self, screenType, **kwargs):
        if not isinstance(screenType, Enum):
            raise RuntimeError(
                "'screenType' param  must be a 'SCREEN_TYPE' instance.")

        screen = SCREEN_LIST[screenType](**kwargs)
        self.root.ids.manager.switch_to(screen)
