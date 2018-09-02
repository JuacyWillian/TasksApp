from kivy.lang import Builder

from . import BaseScreen

task_edit_kv = """

"""


class TaskEditScreen(BaseScreen):
    def on_enter(self, *args):
        Builder.load_string(task_edit_kv)
