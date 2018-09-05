from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.date_picker import MDDatePicker

from tasks.screens import BaseScreen
from tasks.models import db, Task

Builder.load_string("""
#:import MDTextField kivymd.textfields
#:import MDCheckbox kivymd.selectioncontrols
#:import MDLabel kivymd.label


<TaskEditScreen>:
    name: "new_task"
    ScrollView:
        do_scroll_x: False
    BoxLayout:
        orientation:'vertical'
        padding: 10, 10
        pos_hint: {'top': 1}
        size_hint_y: None
        height: self.minimum_height

        MDTextField:
            id: task_name
            hint_text: "Task Name"
            required: True
            helper_text_mode: "on_error"

        MDTextField:
            id: task_body
            hint_text: "Task Description"
            required: True
            helper_text_mode: "on_error"

        BoxLayout:
            size_hint: 1, None
            height: self.minimum_height

            MDCheckbox:
                id: task_finished
                size_hint: None, None
                size: dp(48), dp(48)
                pos_hint: {'center_x': 0.25, 'center_y': 0.5}

            MDLabel:
                font_style: 'Body1'
                text: "finished"
                size_hint: 1, 1
                # height: self.texture_size[1]

        MDTextField:
            id: task_date
            hint_text: "Task Date"
            on_focus: root.show_date_picker(self.text)

        MDTextField:
            id: task_tag
            hint_text: "Task Flag"

""")


class TaskEditScreen(BaseScreen):
    task = ObjectProperty(None)

    def __init__(self, task=None, **kwargs):
        super(TaskEditScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()

        if task:
            self.task = task

    def on_enter(self,):
        super(TaskEditScreen, self).on_enter()
        self.toolbar = self.app.root.ids.toolbar

        if self.task:
            self.ids.task_name.text = self.task.title
            self.ids.task_date.text = str(self.task.date)
            self.ids.task_tag.text = self.task.tag
            self.ids.task_finished.active = self.task.finished

    def on_toolbar(self, *args):
        self.toolbar.title = 'Edit Task'
        self.toolbar.left_action_items = [
            ['arrow-left', lambda x: self.goto_home()]
        ]
        self.toolbar.right_action_items = [
            ['content-save', lambda x: self.save_task()]
        ]

    def save_task(self, ):
        values = dict(
            title=self.ids.task_name.text,
            finished=bool(self.ids.task_finished.active),
            date=datetime.strptime(self.ids.task_date.text, "%Y-%m-%d").date(),
            tag=self.ids.task_tag.text
        )
        if not self.task:
            self.new_task(**values)
        else:
            self.edit_task(**values)

        self.goto_home()

    def show_date_picker(self, date=""):
        self.datepicker = MDDatePicker(self.set_previous_date)
        try:
            year, month, day = [int(i) for i in date.split('-')]
            self.datepicker.year = year
            self.datepicker.month = month
            self.datepicker.day = day
        except:
            pass
        self.datepicker.open()

    def set_previous_date(self, date):
        self.ids.task_date.text = str(date)

    def edit_task(self, **values):
        with db:
            # self.task.__dict__.update(**values)
            for k, v in values.items():
                setattr(self.task, k, v)
            self.task.save()

    def new_task(self, **values):
        with db:
            self.task = Task.create(**values)
            self.task.save()

    def goto_home(self, ):
        from tasks.screens.home_screen import HomeScreen

        self.manager.transition = SlideTransition(direction='right')
        self.manager.switch_to(HomeScreen(name='home'))
