from kivy.lang import Builder
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog


Builder.load_string("""
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
            on_focus: root.show_date_picker()

        MDTextField:
            id: task_tag
            hint_text: "Task Flag"
""")


class EditTaskDialog(MDDialog):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_date_picker(self,):
        self.datepicker = MDDatePicker(self.set_previous_date)
        self.datepicker.open()

    def set_previous_date(self, date):
        text_date = self.ids.task_date
        text_date.text = str(date)
        self.datepicker.dismiss()
