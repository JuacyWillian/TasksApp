import unittest

from kivy.clock import Clock

from tasks import TasksApp
from tasks.screens import SCREENS_TYPE
from tasks.screens.task_edit_screen import TaskEditScreen


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
        # self.app.goto(SCREENS_TYPE.EDIT)
        screen = self.app.root.ids.manager.current_screen
        self.assertIsInstance(screen, TaskEditScreen)

    def test_toolbar_title(self, ): pass

    def test_toolbar_left_action_items(self, ): pass
