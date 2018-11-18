import unittest
from datetime import datetime

from kivy.clock import Clock

from tasks import TasksApp
from tasks.models import Task, db
from tasks.screens import SCREENS_TYPE
from tasks.screens.task_edit_screen import TaskEditScreen
from tests.utils import *


class EditTaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = TasksApp()
        Clock.schedule_interval(lambda *x: self.app.stop(), 0.000001)
        self.app.run()

        self.task = self.create_task()

        self.app.goto(SCREENS_TYPE.EDIT, task=self.task)
        self.toolbar = self.app.root.ids.toolbar

    def create_task(self, ):
        values = dict(
            title="Conta de Luz",
            finished=False,
            date=datetime.now().date(),
            tag="conta"
        )
        with db:
            task = Task.create(**values)
            task.save()
            return task

    def test_edit_task_screen_name(self, ):
        screen = self.app.root.ids.manager.current
        self.assertEqual(screen, 'edit_task')

    def test_edit_task_type(self, ):
        screen = self.app.root.ids.manager.current_screen
        self.assertIsInstance(screen, TaskEditScreen)

    def test_task_info(self, ):
        self.assertEqual(get_screen_element(
            self.app, 'task_name').text, self.task.title)

        self.assertEqual(get_screen_element(
            self.app, 'task_tag').text, self.task.tag)

        self.assertEqual(get_screen_element(
            self.app, 'task_finished').active, self.task.finished)

        self.assertEqual(get_screen_element(
            self.app, 'task_date').text, str(self.task.date))

    def test_toolbar_title(self, ):
        """Testa se o titulo da toolbar é 'Edit Task'."""
        self.assertEqual(self.app.root.ids.toolbar.title, 'Edit Task')

    def test_toolbar_left_action_items(self, ):
        """Testa se a toolbar possui o botao 'salvar'."""
        self.assertEqual(len(self.toolbar.right_action_items), 1)
