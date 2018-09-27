import unittest

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

from tasks import TasksApp
from tasks.screens import SCREENS_TYPE
from tasks.screens.home_screen import HomeScreen
from tasks.screens.task_edit_screen import TaskEditScreen


class TasksAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = TasksApp()
        Clock.schedule_interval(lambda *x: self.app.stop(), 0.000001)
        self.app.run()

    def test_app_infos(self, ):
        self.assertEqual(self.app.get_application_name(), 'Tasks')
        self.assertEqual(self.app.website,
                         'http://juacywillian.github.io/tasks')

    def test_app_build(self, ):
        self.assertIsInstance(self.app.root, BoxLayout)
        self.assertIsNotNone(self.app.root.ids.toolbar)
        self.assertIsNotNone(self.app.root.ids.manager)

    def test_goto(self, ):
        self.assertRaises(TypeError, self.app.goto, 'home')
        self.assertRaises(TypeError, self.app.goto, 1)
        self.assertRaisesRegex(
            TypeError, r".* 'SCREEN_TYPE' instance\.$",
            self.app.goto, 'home')
