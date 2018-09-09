from datetime import datetime
from enum import Enum

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.uix.scrollview import ScrollView
from kivymd.menu import MDDropdownMenu
from kivymd.toolbar import Toolbar

from tasks.components.list import TaskList, TaskListItem
from tasks.models import Task, db
from tasks.screens import SCREENS_TYPE, BaseScreen
from tasks.screens.about_screen import AboutScreen
from tasks.screens.task_edit_screen import TaskEditScreen


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

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()

    def on_enter(self, ):
        super(HomeScreen, self).on_enter()

        Clock.schedule_once(self.load_tasks)
        tasklist = self.ids.task_list
        tasklist.on_selected_item = self.show_menu
        self.toolbar: Toolbar = self.app.root.ids.toolbar

    def on_toolbar(self, *args):
        self.toolbar.title = self.app.get_application_name()
        self.toolbar.left_action_items = []
        self.toolbar.right_action_items = [
            ['plus', lambda x: self.app.goto(SCREENS_TYPE.EDIT)],
            # ['dots-vertical', self.show_tb_menu]
            ['information-outline', lambda x: self.app.goto(SCREENS_TYPE.ABOUT)]
        ]

    def show_tb_menu(self, button):
        menu_items = [
            # {'viewclass': 'MDMenuItem', 'text': 'sort',
            #  'on_release': lambda: self.show_sort_menu()},
            # {'viewclass': 'MDMenuItem', 'text': 'filter',
            #  'on_release': lambda: self.show_filter_menu()},
            {'viewclass': 'MDMenuItem', 'text': 'about',
             'on_release': lambda: self.app.goto(SCREENS_TYPE.ABOUT)},
        ]

        MDDropdownMenu(items=menu_items, width_mult=4).open(button)

    def show_filter_menu(self, ):
        pass

    def show_sort_menu(self, ):
        pass

    def goto_about(self, ):
        pass

    def on_tasks_list(self, *args):
        tasklist = self.ids.task_list
        if tasklist:
            tasklist.clear_widgets()
            for t in self.tasks_list:
                tasklist.add_task(t)

    def load_tasks(self, *args):
        self.tasks_list = []
        self.tasks_list = Task.select().order_by(Task.date)

    def show_menu(self, item: TaskListItem):
        _item = item.get_item()
        menu_items = [
            {'viewclass': 'MDMenuItem', 'text': 'edit',
             'on_release': lambda: self.app.goto(SCREENS_TYPE.EDIT, task=_item)},
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
