# coding= utf-8
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.toolbar import Toolbar

from tasks.screens import BaseScreen, SCREENS_TYPE

Builder.load_string("""
#:import hexColor kivy.utils.get_color_from_hex
#:import MDLabel kivymd.label

<AboutScreen>:
    name: 'about'
    ScrollView:
        do_scroll_x: False
        BoxLayout:
            orientation: 'vertical'
            padding: 10, 10
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
                text: u'Version: '+app.version
                halign: 'center'

            MDLabel:
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'Subhead'
                text: app.description
                halign: 'justify'
                padding: 10, 10

            MDLabel:
                text: '[b]Developers:[/b] %s'%(", ".join(['[ref='+d[1]+']'+d[0]+'[/ref]' for d in app.developers]))
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'Body1'
                markup: True
                on_ref_press:
                    import webbrowser
                    webbrowser.open(args[1])

            MDLabel:
                text: 'website: [ref='+app.website+']'+app.website+'[/ref]'
                markup: True
                size_hint_y: None
                height: self.texture_size[1]
                font_style: 'Body2'
                on_ref_press:
                    import webbrowser
                    webbrowser.open(args[1])
""")


class AboutScreen(BaseScreen):
    app = ObjectProperty(None)

    def __init__(self, app, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)
        self.app = app

    def on_enter(self, ):
        super(AboutScreen, self).on_enter()
        self.toolbar = self.app.root.ids.toolbar
        self.toolbar = Toolbar(id='toolbar')

    def on_toolbar(self, *args):
        self.toolbar.title = 'About'
        self.toolbar.left_action_items = [
            ['arrow-left', lambda *x: self.app.goto(SCREENS_TYPE.HOME)]
        ]
        self.toolbar.right_action_items = []
