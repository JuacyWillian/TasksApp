# coding= utf-8
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty, OptionProperty
from kivymd.menu import MDDropdownMenu
from kivymd.toolbar import Toolbar

from tasks.models import Task, db
from tasks.screens import BaseScreen, SCREENS_TYPE

Builder.load_string("""
#:import MDFloatingActionButton kivymd.button
#:import TaskList tasks.components.list

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

    def __init__(self, app, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.app = app

    def on_enter(self, ):
        super(HomeScreen, self).on_enter()

        Clock.schedule_once(self.load_tasks)
        tasklist = self.ids.task_list
        tasklist.on_selected_item = self.show_menu
        # self.app.root.replace()
        self.toolbar = self.app.root.ids.toolbar
        self.toolbar = Toolbar(id='toolbar')

    def on_toolbar(self, *args):
        """Configure Toolbar."""
        self.toolbar.title = self.app.get_application_name()
        self.toolbar.left_action_items = []
        self.toolbar.right_action_items = [
            ['plus', lambda x: self.app.goto(SCREENS_TYPE.EDIT)],
            # ['dots-vertical', self.show_tb_menu]
            ['information-outline',
             lambda x: self.app.goto(SCREENS_TYPE.ABOUT)]
        ]

    def show_filter_menu(self, ):
        """Show filter task menu."""
        pass

    def show_sort_menu(self, ):
        """Show sort task menu."""
        pass

    def goto_about(self, ):
        pass

    def on_tasks_list(self, *args):
        """Update task list."""
        tasklist = self.ids.task_list
        if tasklist:
            tasklist.clear_widgets()
            for t in self.tasks_list:
                tasklist.add_task(t)

    def load_tasks(self, *args):
        """Load all tasks from database. sorting by task.date."""
        self.tasks_list = []
        self.tasks_list = Task.select().order_by(Task.date)

    def show_menu(self, item):
        """Show selected item menu."""
        _item = item.get_item()
        menu_items = [
            {'viewclass': 'MDMenuItem', 'text': 'edit',
             'callback': lambda x: self.app.goto(SCREENS_TYPE.EDIT, task=_item)},
            {'viewclass': 'MDMenuItem', 'text': 'remove',
             'callback': lambda x: self.remove_task(_item)},
            {'viewclass': 'MDMenuItem', 'text': 'mark as finished',
             'callback': lambda x: self.mark_as_finished(_item)},
        ]
        MDDropdownMenu(items=menu_items, width_mult=4).open(item)

    def remove_task(self, task):
        """Remove selected task from database."""
        with db:
            task.delete_instance()
        self.load_tasks()

    def mark_as_finished(self, task):
        """Mark selected task as finished."""
        with db:
            task.finished = True
            task.save()
        self.load_tasks()
