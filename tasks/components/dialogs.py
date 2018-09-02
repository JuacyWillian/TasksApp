from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog

from ..models import Task

Builder.load_string("""
#:import MDTextField kivymd.textfields
#:import MDCheckbox kivymd.selectioncontrols
#:import MDLabel kivymd.label


<EditTaskDialog>:
    title: "New Task"
    size_hint: .8, .75
    # height: self.content.height
    auto_dismiss: True
    BoxLayout:
        orientation:'vertical'
        size_hint: 1, None
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


class EditTaskDialog(MDDialog):
    task: Task = ObjectProperty(None)

    def __init__(self, task=None, **kwargs):
        super().__init__(**kwargs)
        self.task = task

    def on_open(self, *args):
        if self.task:
            self.ids.task_name = self.task.title
            # self.ids.task_body = self.task.body
            self.ids.task_date = self.task.date
            self.ids.task_tag = self.task.tag

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
        text_date = self.ids.task_date
        text_date.text = str(date)
        # self.datepicker.dismiss()
