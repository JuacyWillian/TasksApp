from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import FadeTransition
from kivymd.label import MDLabel

from tasks.screens import SCREENS_TYPE, BaseScreen


Builder.load_string("""
#:import hexColor kivy.utils.get_color_from_hex
#:import MDLabel kivymd.label

<AboutScreen>:
    ScrollView:
        do_scroll_x: False
        BoxLayout:
            orientation: 'vertical'
            # padding: 10, 10
            size_hint_y: None
            height: self.minimum_height
            pos_hint: {'top': 1}

            AsyncImage:
                canvas.before:
                    Color:
                        rgba: hexColor('#008080')
                    Rectangle:
                        pos: self.pos
                        size: self.size
                size_hint: 1, None
                height: 200
                source: app.logo
                keet_ratio: False
                allow_strech: False

            MDLabel:
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'Headline'
                text: app.get_application_name()
                halign: 'center'

            MDLabel:
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'Subhead'
                text: f'v{app.version}'
                halign: 'center'

            MDLabel:
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'Subhead'
                text: f'{app.description}'
                halign: 'justify'
                padding: 10, 10

            MDLabel:
                text: f'[b]Developers:[/b] {", ".join(app.developers)}'
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'Body1'
                markup: True
                padding: 10, 10

            MDLabel:
                text: f'website: [ref={app.website}]{app.website}[/ref]'
                markup: True
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'Body2'
                padding: 10, 10
                on_ref_press:
                    import webbrowser
                    webbrowser.open(args[1])
""")


class AboutScreen(BaseScreen):
    app = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(AboutScreen, self). __init__(**kwargs)
        self.app = App.get_running_app()

    def on_enter(self, ):
        super(AboutScreen, self).on_enter()
        self.toolbar = self.app.root.ids.toolbar

    def on_toolbar(self, *args):
        self.toolbar.title = 'About'
        self.toolbar.left_action_items = [
            ['arrow-left', lambda *x: self.app.goto(SCREENS_TYPE.HOME)]
        ]
        self.toolbar.right_action_items = []