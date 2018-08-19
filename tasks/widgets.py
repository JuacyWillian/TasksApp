from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.relativelayout import RelativeLayout
from kivymd.button import *
from kivymd.label import MDLabel
from kivymd.list import *
from kivymd.navigationdrawer import *


Builder.load_string("""
<IconLeftSampleWidget>:
<IconRightSampleWidget>:
<MDIcon>:
""")


class MDIcon(MDLabel):
    icon = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_style: 'Icon'

    def on_icon(self, instance, value):
        self.text: u"{}".format(md_icons[root.icon])
        return True


class IconLeftSampleWidget(ILeftBody, MDIconButton):
    def __init__(self, task, **kwargs):
        super().__init__(**kwargs)

        self.icon = f"checkbox-{'marked' if task.finished else 'blank'}-outline"


class IconRightSampleWidget(IRightBodyTouch, MDIconButton):
    pass
