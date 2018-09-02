from datetime import datetime

from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.scrollview import ScrollView
from kivymd.menu import MDDropdownMenu

from . import BaseScreen
from ..components import TaskList, TaskListItem, toolbar
from ..components.dialogs import EditTaskDialog
from ..models import Task

home_kv = """
#:import MDFloatingActionButton kivymd.button

<HomeScreen>:       
    MDFloatingActionButton:
        icon: 'plus'
        pos_hint: {'right': .95, 'y': .05}
        on_release: root.show_new_task_dialog()
"""


class HomeScreen(BaseScreen):
    tasks_list = ListProperty([])
    tasks = ObjectProperty(None)
    toolbar = ObjectProperty()

    def on_enter(self, ):
        Builder.load_string(home_kv)
        self.toolbar = toolbar()

        scroll = ScrollView(do_scroll_x=False)
        self.tasks = TaskList(
            [], id='taskList',
            on_selected_item=lambda item: self.show_menu(item)
        )
        scroll.add_widget(self.tasks)
        self.add_widget(scroll)
        self.tasks_list = Task.select()

    def on_tasks_list(self, *args):
        self.load_tasks()

    def load_tasks(self, filter=None, sort=None, limit=None):
        if self.tasks:
            self.tasks.clear_widgets()
            for t in self.tasks_list:
                self.tasks.add_task(t)

    def on_toolbar(self, *args):
        if self.toolbar:
            self.toolbar.title = "Task List"

    def show_new_task_dialog(self, task=None, callback=None):
        dialog = EditTaskDialog(task)
        dialog.add_action_button("Dismiss", lambda *x: dialog.dismiss())
        if callback:
            dialog.add_action_button("Edit", lambda *x: callback(dialog))
        else:
            dialog.add_action_button(
                "Create", lambda *x: self.create_task(dialog))
        dialog.open()

    def edit_task(self, dialog, ):
        print(dialog)

    def create_task(self, dialog):
        data = datetime.strptime(dialog.ids.task_date.text, "%Y-%m-%d")

        task = Task.create(
            title=dialog.ids.task_name.text,
            finished=dialog.ids.task_finished.active,
            date=data.date(),
            tag=dialog.ids.task_tag.text
        )
        task.save()
        dialog.dismiss()
        self.tasks_list.append(task)

    def show_menu(self, item: TaskListItem):
        _item = item.get_item()
        menu_items = [
            {'viewclass': 'MDMenuItem', 'text': 'edit',
             'on_release': lambda: self.show_new_task_dialog(_item)},
            {'viewclass': 'MDMenuItem', 'text': 'remove',
             'on_release': lambda: self.remove_item(_item)},
            {'viewclass': 'MDMenuItem', 'text': 'mark as finished',
             'on_release': lambda: self.mark_as_finished(_item)},
        ]

        MDDropdownMenu(items=menu_items, width_mult=4).open(item)
