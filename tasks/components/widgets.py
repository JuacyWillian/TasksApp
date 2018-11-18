# coding= utf-8
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.button import MDIconButton
from kivymd.label import MDLabel
from kivymd.list import IRightBodyTouch
from kivymd.navigationdrawer import ILeftBody

Builder.load_string("""
<IconLeftSampleWidget>:
<IconRightSampleWidget>:
<MDIcon>:
""")


class MDIcon(MDLabel):
    icon = StringProperty('')

    def __init__(self, **kwargs):
        super(MDIcon, self).__init__(**kwargs)

        self.font_style = 'Icon'

    def on_icon(self, instance, value):
        self.text = u"{}".format(md_icons[root.icon])
        return True


class IconLeftSampleWidget(ILeftBody, MDIconButton):
    def __init__(self, task, **kwargs):
        super(IconLeftSampleWidget, self).__init__(**kwargs)
        self.icon = "checkbox-" + \
                    ('marked' if task.finished else 'blank') + "-outline"


class IconRightSampleWidget(IRightBodyTouch, MDIconButton):
    pass
