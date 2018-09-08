from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.list import MDList, TwoLineIconListItem

from tasks.components.widgets import IconLeftSampleWidget
from tasks.models import Task, db


Builder.load_string("""
<TaskList>:

<TaskListItem>:
""")


class TaskListItem(TwoLineIconListItem):
    item = ObjectProperty(None)

    def __init__(self, task: Task, **kwargs):
        super(TaskListItem, self).__init__(**kwargs)

        self.item = task
        self.text = task.title
        self.secondary_text = f"{task.date}{10*' '}{task.tag}"
        self.add_widget(IconLeftSampleWidget(task))

    def get_item(self, ):
        return self.item


class TaskList(MDList):
    selected_item = ObjectProperty(None)

    def __init__(self, items=[], **kwargs):
        super(TaskList, self).__init__(**kwargs)

        self.on_selected_item = kwargs.get(
            'on_selected_item', self.on_selected_item)
        for i in items:
            self.add_task(i)

    def add_task(self, task):
        self.add_widget(TaskListItem(
            task, on_release=self.on_selected_item))

    def on_selected_item(self, *args):
        pass
