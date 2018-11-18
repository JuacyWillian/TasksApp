# coding= utf-8
import calendar
from datetime import date, datetime

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel

from tasks.models import Task, db
from tasks.screens import BaseScreen, SCREENS_TYPE

Builder.load_string("""
#:import MDTextField kivymd.textfields
#:import MDCheckbox kivymd.selectioncontrols
#:import MDLabel kivymd.label

<TaskEditScreen>:
    name: "new_task" if not self.task else "edit_task"
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
                on_focus: root.show_date_picker(self)

            MDTextField:
                id: task_tag
                hint_text: "Task Flag"
""")


class TaskEditScreen(BaseScreen):
    task = ObjectProperty(None)
    dialog = ObjectProperty(None)

    def __init__(self, app, task=None, **kwargs):
        super(TaskEditScreen, self).__init__(**kwargs)
        self.app = app

        if task:
            self.task = task

    def on_pre_enter(self, ):
        super(TaskEditScreen, self).on_enter()
        self.toolbar = self.app.root.ids.toolbar

        if self.task:
            self.ids.task_name.text = self.task.title
            self.ids.task_date.text = str(self.task.date)
            self.ids.task_tag.text = self.task.tag
            self.ids.task_finished.active = self.task.finished

    def on_toolbar(self, *args):
        self.toolbar.title = 'Edit Task' if self.task else 'New Task'
        self.toolbar.left_action_items = [
            ['arrow-left', lambda x: self.app.goto(SCREENS_TYPE.HOME)]
        ]
        self.toolbar.right_action_items = [
            ['content-save', lambda x: self.save_task()]
        ]

    def save_task(self, ):
        errors = []

        title = self.ids.task_name.text
        if len(title.replace(' ', '')) == 0:
            errors.append("Field 'title' is required.")

        try:
            data = datetime.strptime(
                self.ids.task_date.text, "%Y-%m-%d").date()
        except:
            data = ''

        if not isinstance(data, date):
            errors.append("Field 'date' is required.")

        if errors:
            self.show_error_dialog(errors)
            return

        values = dict(
            title=title,
            finished=bool(self.ids.task_finished.active),
            date=data,
            tag=self.ids.task_tag.text
        )
        if not self.task:
            self.new_task(**values)
        else:
            self.edit_task(**values)

        self.app.goto(SCREENS_TYPE.HOME)

    def show_error_dialog(self, errors):
        content = MDLabel(
            text='\n\n' + '\n'.join(errors),
            padding=(10, 10),
            theme_text_color='Error'
        )
        dialog = MDDialog(
            title='Errors',
            content=content,
            size_hint=(.75, .5))
        dialog.add_action_button('close', dialog.dismiss)
        dialog.open()

    def show_date_picker(self, instance):
        if instance.focus:
            date = instance.text

            def set_previous_date(date):
                self.ids.task_date.text = str(date)
                try:
                    dialog.dismiss()
                except:
                    pass

            dialog = MDDatePicker(
                set_previous_date, firstweekday=calendar.SUNDAY,
                auto_dismiss=False)

            try:
                year, month, day = [int(i) for i in date.split('-')]
                dialog.set_date(year, month, day)
            except:
                pass
            finally:
                dialog.open()

    def edit_task(self, **values):
        with db:
            for k, v in values.items():
                setattr(self.task, k, v)
            self.task.save()

    def new_task(self, **values):
        with db:
            self.task = Task.create(**values)
            self.task.save()
