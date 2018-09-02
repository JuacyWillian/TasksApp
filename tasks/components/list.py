from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivymd.list import MDList, TwoLineIconListItem

from .widgets import IconLeftSampleWidget
from ..models import Task

list_kv = """
<TaskList>:
"""

list_item_kv = """
<TaskListItem>:
"""


class TaskListItem(TwoLineIconListItem):
    item = ObjectProperty(None)

    def __init__(self, task: Task, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(list_kv)
        self.item = task
        self.text = task.title
        self.secondary_text = f"{task.date}{10*' '}{task.tag}"
        self.add_widget(IconLeftSampleWidget(task))

    def get_item(self, ):
        return self.item


class TaskList(MDList):
    items = ListProperty([])
    selected_item = None

    def __init__(self, items, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(list_item_kv)
        self.items = items
        self.on_selected_item = kwargs.get('on_selected_item', None)
        for i in self.items:
            self.add_task(i)

    def add_task(self, task):
        self.add_widget(TaskListItem(task, on_release=self.on_selected_item))
