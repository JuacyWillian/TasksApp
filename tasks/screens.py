from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from tasks.components import TaskList
from tasks.dialogs import EditTaskDialog
from tasks.models import Task, db


Builder.load_string("""
<HomeScreen>:
    MDFloatingActionButton:
        icon: 'plus'
        pos_hint: {'right': .95, 'y': .05}
        on_release: root.show_new_task_dialog()


<TaskEditScreen>:

""")


class BaseScreen(Screen):
    def on_pre_enter(self, *args):
        super().on_pre_enter(*args)
        db.connection()

    def on_enter(self, *args):
        super().on_enter(*args)

    def on_pre_leave(self, *args):
        super().on_pre_leave(*args)

    def on_leave(self, *args):
        super().on_leave(*args)
        db.close()


class HomeScreen(BaseScreen):
    tasks_list = ListProperty([])
    tasks = ObjectProperty(None)
    toolbar = ObjectProperty()

    def on_tasks_list(self, *args):
        self.load_tasks()

    def on_enter(self,):
        self.configure_toolbar()
        scroll = ScrollView(do_scroll_x=False)
        self.tasks = TaskList([], id='taskList')
        scroll.add_widget(self.tasks)
        self.add_widget(scroll)

        self.tasks_list = Task.select()

    def configure_toolbar(self, ):
        app = App.get_running_app()

    def load_tasks(self, filter=None, sort=None, limit=None):
        if self.tasks:
            self.tasks.clear_widgets()
            for t in self.tasks_list:
                self.tasks.add_task(t)

    def on_toolbar(self, *args):
        if toolbar:
            print(toolbar)

    def show_new_task_dialog(self, *args):
        dialog = EditTaskDialog()
        dialog.add_action_button("Dismiss", lambda *x: dialog.dismiss())
        dialog.add_action_button("Create", lambda *x: self.create_task(dialog))
        dialog.open()

    def create_task(self, dialog):
        data = datetime.strptime(dialog.ids.task_date.text, "%Y-%m-%d")

        task = Task.create(
            title=dialog.ids.task_name.text,
            # body=dialog.ids.task_body.text,
            finished=dialog.ids.task_finished.active,
            date=data.date(),
            tag=dialog.ids.task_tag.text
        )
        task.save()
        dialog.dismiss()
        self.tasks_list.append(task)


class TaskEditScreen(BaseScreen):

    def on_enter(self, *args):
        super().on_enter(*args)

    def on_pre_leave(self, *args):
        super().on_pre_leave(*args)
