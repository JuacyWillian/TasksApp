import unittest
from datetime import datetime

from kivy.clock import Clock
from kivymd.selectioncontrols import MDCheckbox
from kivymd.textfields import MDTextField

from tasks import TasksApp
from tasks.screens import SCREENS_TYPE
from tasks.screens.home_screen import HomeScreen
from tasks.screens.task_edit_screen import TaskEditScreen
from tests.utils import get_screen_element


class NewTaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = TasksApp()
        Clock.schedule_interval(lambda *x: self.app.stop(), 0.000001)
        self.app.run()

        self.app.goto(SCREENS_TYPE.EDIT)
        self.toolbar = self.app.root.ids.toolbar

    def test_new_task_screen_name(self, ):
        screen = self.app.root.ids.manager.current
        self.assertEqual(screen, 'new_task')

    def test_new_task_type(self, ):
        screen = self.app.root.ids.manager.current_screen
        self.assertIsInstance(screen, TaskEditScreen)

    def test_if_elements_exists(self, ):
        self.assertIsNotNone(get_screen_element(self.app, 'task_name'))
        self.assertIsNotNone(get_screen_element(self.app, 'task_tag'))
        self.assertIsNotNone(get_screen_element(self.app, 'task_finished'))
        self.assertIsNotNone(get_screen_element(self.app, 'task_date'))

    def test_elements_type(self, ):
        self.assertIsInstance(get_screen_element(
            self.app, 'task_name'), MDTextField)
        self.assertIsInstance(get_screen_element(
            self.app, 'task_tag'), MDTextField)
        self.assertIsInstance(get_screen_element(
            self.app, 'task_finished'), MDCheckbox)
        self.assertIsInstance(get_screen_element(
            self.app, 'task_date'), MDTextField)

    def test_save_task(self, ):
        get_screen_element(self.app, 'task_name').text = 'hola'
        get_screen_element(self.app, 'task_tag').text = 'mundo'
        get_screen_element(self.app, 'task_finished').active = True
        get_screen_element(self.app, 'task_date').text = str(
            datetime.now().date())

        self.app.root.ids.manager.current_screen.save_task()

        self.assertIsInstance(self.app.root.ids.manager.current_screen, HomeScreen)
