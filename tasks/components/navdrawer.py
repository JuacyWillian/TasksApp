from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivymd.navigationdrawer import NavigationDrawerHeaderBase
from kivymd.theming import ThemableBehavior

navdrawer_kv = """
#:import MDLabel kivymd.label

<NavigationDrawerHeader>:
    size_hint: 1, None
    height: 200
    AsyncImage:
        canvas:
            Color:
                rgba: root.background_color if not root.background_image else [1, 1, 1, 1]
            Rectangle:
                pos: self.pos
                size: self.size
                source: self.source if root.background_image else None
        source: root.background_image
        pos: 0,0
        size: root.size

    MDLabel:
        text: root.title
        font_style: 'Title'
        size_hint: 1, None
        height: self.texture_size[1]
        padding: 10, 10
        pos: 15, 25
        theme_text_color: 'Custom'
        text_color: root.title_color

    MDLabel:
        text: root.subtitle
        font_style: 'Subhead'
        theme_text_color: 'Custom'
        text_color: root.subtitle_color
        size_hint: 1, None
        height: self.texture_size[1]
        padding: 10, 10
        pos: 15, 0

    AsyncImage:
        source: root.avatar if root.avatar else 'data/image/avatar_default.jpg'
        pos: 25, 75
        size_hint: None, None
        size: 100, 100
        padding: 10, 10
        canvas:
            Clear
            Color:
                rgba: 1,1,1,1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [100]
                texture: self.texture

            Color:
                rgba: root.avatar_circle_color
            SmoothLine:
                circle: self.center_x, self.center_y, self.width//2
"""


class NavigationDrawerHeader(
    RelativeLayout, ThemableBehavior,
    RectangularElevationBehavior, NavigationDrawerHeaderBase):
    title = StringProperty('')
    title_color = ListProperty([1, 1, 1, 1])

    subtitle = StringProperty('')
    subtitle_color = ListProperty([1, 1, 1, 1])

    background_image = StringProperty('data/image/navHeader_bg.jpg')
    background_color = ListProperty([0, 0, 0, 1])

    avatar = StringProperty('')
    avatar_circle_color = ListProperty([1, 1, 1, 1])

    def __init__(self, **kw):
        super().__init__(**kw)
        Builder.load_string(navdrawer_kv)
        self.title = App.get_running_app().get_application_name()
        self.subtitle = 'juacy.willian@gmail.com'
