from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.uix.scrollview import ScrollView
from kivymd.menu import MDDropdownMenu
from kivymd.toolbar import Toolbar

from tasks.screens import BaseScreen
from tasks.screens.task_edit_screen import TaskEditScreen
from tasks.components import TaskList, TaskListItem, toolbar
from tasks.components.dialogs import EditTaskDialog
from tasks.models import db, Task

Builder.load_string("""
#:import MDFloatingActionButton kivymd.button
#:import TaskList tasks.components

<HomeScreen>:
    name: 'home'
    ScrollView:
        id: scrollview
        size_hint: 1,1
        TaskList:
            id: task_list
            size_hint: 1,1
            on_selected_item: lambda item: self.show_menu(item)

""")


class HomeScreen(BaseScreen):
    tasks_list = ListProperty([])
    tasks = ObjectProperty(None)

    sort_by = OptionProperty('date__desc', options=['date', 'date__desc'])
    filter_by = OptionProperty(
        'pending', options=['none', 'pending', 'finished'])
    limit = OptionProperty(25, options=[25, 50, 100, 150])

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()

    def goto_new_task(self,):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.switch_to(TaskEditScreen(name='new_task'))

    def on_enter(self, ):
        super(HomeScreen, self).on_enter()

        Clock.schedule_once(self.load_tasks)
        tasklist = self.ids.task_list
        tasklist.on_selected_item = self.show_menu
        self.toolbar: Toolbar = self.app.root.ids.toolbar

    def on_toolbar(self, *args):
        self.toolbar.title = self.app.get_application_name()

        self.toolbar.left_action_items = [
            ['menu', lambda x: self.app.root.toggle_nav_drawer()]
        ]
        self.toolbar.right_action_items = [
            ['plus', lambda x: self.goto_new_task()]
        ]

    def show_tb_menu(self, button):
        menu_items = [
            {'viewclass': 'MDMenuItem', 'text': 'edit',
             'on_release': lambda: self.manager.switch_to(TaskEditScreen(_item))},
            {'viewclass': 'MDMenuItem', 'text': 'remove',
             'on_release': lambda: self.remove_item(_item)},
            {'viewclass': 'MDMenuItem', 'text': 'mark as finished',
             'on_release': lambda: self.mark_as_finished(_item)},
        ]

        MDDropdownMenu(items=menu_items, width_mult=4).open(button)

    def on_tasks_list(self, *args):
        tasklist = self.ids.task_list
        if tasklist:
            tasklist.clear_widgets()
            for t in self.tasks_list:
                tasklist.add_task(t)

    def load_tasks(self, *args):
        self.tasks_list = []
        self.tasks_list = Task.select()

    def show_menu(self, item: TaskListItem):
        _item = item.get_item()
        menu_items = [
            {'viewclass': 'MDMenuItem', 'text': 'edit',
             'on_release': lambda: self.manager.switch_to(TaskEditScreen(name='edit_task', task=_item))},
            {'viewclass': 'MDMenuItem', 'text': 'remove',
             'on_release': lambda: self.remove_task(_item)},
            {'viewclass': 'MDMenuItem', 'text': 'mark as finished',
             'on_release': lambda: self.mark_as_finished(_item)},
        ]

        MDDropdownMenu(items=menu_items, width_mult=4).open(item)

    def remove_task(self, task: Task):
        with db:
            task.delete_instance()
        self.load_tasks()

    def mark_as_finished(self, task: Task):
        with db:
            task.finished = True
            task.save()
        self.load_tasks()
