import unittest
from datetime import datetime

from kivy.clock import Clock

from tasks import TasksApp
from tasks.screens import SCREENS_TYPE
from tasks.screens.task_edit_screen import TaskEditScreen

from tasks.models import db, Task


class EditTaskTestCase(unittest.TestCase):
    pass

    # def setUp(self):
    #     self.app = TasksApp()
    #     Clock.schedule_interval(lambda *x: self.app.stop(), 0.000001)
    #     self.app.run()

    #     self.task = self.create_task()

    #     self.app.goto(SCREENS_TYPE.EDIT, task=self.task)
    #     self.toolbar = self.app.root.ids.toolbar

    # def create_task(self, ):
    #     values = dict(
    #         title="Conta de Luz",
    #         finished=False,
    #         date=datetime.now().date,
    #         tag="conta"
    #     )
    #     with db:
    #         task = Task.create(**values)
    #         task.save()
    #         return task

    # def test_edit_task_screen_name(self, ):
    #     screen = self.app.root.ids.manager.current
    #     self.assertEqual(screen, 'edit_task')

    # def test_edit_task_type(self, ):
    #     screen = self.app.root.ids.manager.current_screen
    #     self.assertIsInstance(screen, TaskEditScreen)

    # def test_toolbar_title(self, ):
    #     title = self.app.root.ids.toolbar.title
    #     self.assertEqual(title, 'Edit Task')

    # def test_toolbar_left_action_items(self, ): pass
