from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import FadeTransition

from . import BaseScreen

splash_kv = """
<SplashScreen>:
    canvas:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size
    size_hint: 1, 1
    pos: 0, 0

    AsyncImage:
        source: root.logo
        size_hint: 1, 1
        keep_ratio: True
        allow_strech: False
"""


class SplashScreen(BaseScreen):
    background_color = ListProperty([0, 0, 0, 1])
    logo = StringProperty('data/image/splash2.png')

    def on_enter(self, ):
        Builder.load_string(splash_kv)
        Clock.schedule_once(self.goto_home, 10 if self.logo else 1)

    def goto_home(self, *args):
        self.manager.transition = FadeTransition()
        self.manager.current = 'home'
