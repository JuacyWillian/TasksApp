from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import FadeTransition

# from tasks.screens import RootLayout

Builder.load_string("""
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
""")


class SplashScreen(FloatLayout):
    app = ObjectProperty(None)
    background_color = ListProperty([0, 0, 0, 1])
    logo = StringProperty('data/image/splash2.png')

    def __init__(self, **kwargs):
        super(SplashScreen, self). __init__(**kwargs)
        self.app = App.get_running_app()
        Clock.schedule_once(self.goto_home, 10 if self.logo else 1)

    def goto_home(self, *args):
        root = RootLayout()
        self.app.root = root
