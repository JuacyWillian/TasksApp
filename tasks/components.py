from kivy.app import App
from kivy.lang import Builder
from kivymd.list import *
from kivymd.navigationdrawer import *
from kivymd.menu import MDDropdownMenu

from tasks.widgets import *
from tasks.models import db, Task


# from kivy. import


Builder.load_string("""
<NavigationDrawerHeader>:
    size_hint: 1, None
    height: 200
    AsyncImage:
        source: root.source
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
        source: root.avatar if root.avatar else 'data/avatar_default.jpg'
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

<TaskListItem>:
<TaskList>:
""")


class NavigationDrawerHeader(RelativeLayout, ThemableBehavior, RectangularElevationBehavior, NavigationDrawerHeaderBase):
    title = StringProperty()
    title_color = ListProperty([1, 1, 1, 1])

    subtitle = StringProperty('')
    subtitle_color = ListProperty([1, 1, 1, 1])

    source = StringProperty('data/navHeader_bg.jpg')
    avatar = StringProperty('')
    avatar_circle_color = ListProperty([1, 1, 1, 1])

    def __init__(self, **kw):
        super().__init__(**kw)
        self.title = App.get_running_app().get_application_name()
        self.subtitle = 'juacy.willian@gmail.com'


class TaskListItem(TwoLineIconListItem):
    task = ObjectProperty(None)

    def __init__(self, task: Task, **kwargs):
        super().__init__(**kwargs)
        self.task = task
        self.text = task.title
        self.secondary_text = f"{task.date}{10*' '}{task.tag}"
        self.add_widget(IconLeftSampleWidget(task))

    def get_item(self, ):
        return self.task


class TaskList(MDList):
    menu_items = [
        {'viewclass': 'MDMenuItem', 'text': 'edit',
            'on_release': lambda: self.edit()},
        {'viewclass': 'MDMenuItem', 'text': 'remove',
            'on_release': lambda: self.remove_item()},
        {'viewclass': 'MDMenuItem', 'text': 'mark as finished',
            'on_release': lambda: self.mark_as_finished()},
    ]
    items = ListProperty([])
    selected_item = None

    def __init__(self, items, **kwargs):
        super().__init__(**kwargs)
        self.items = items
        for i in self.items:
            self.add_task(i)

    def add_task(self, task):
        self.add_widget(TaskListItem(task, on_press=self.on_selected_item))

    def on_selected_item(self, selected):
        selected_item = selected.get_item()
        MDDropdownMenu(items=self.menu_items, width_mult=4).open(selected)

    def menu(self, *args):
        print(*args)
