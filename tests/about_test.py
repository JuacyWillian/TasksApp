import unittest

from kivy.clock import Clock

from tasks import TasksApp
from tasks.screens import SCREENS_TYPE
from tasks.screens.about_screen import AboutScreen


class AboutTestCase(unittest.TestCase):
    def setUp(self):
        self.app = TasksApp()
        Clock.schedule_interval(lambda *x: self.app.stop(), 0.000001)
        self.app.run()

        self.app.goto(SCREENS_TYPE.ABOUT)
        self.toolbar = self.app.root.ids.toolbar

    def test_about_screen_name(self, ):
        screen = self.app.root.ids.manager.current
        self.assertEqual(screen, 'about')

    def test_about_screen_type(self, ):
        screen = self.app.root.ids.manager.current_screen
        self.assertIsInstance(screen, AboutScreen)

    def test_toolbar_title(self, ): pass

    def test_toolbar_left_action_items(self, ): pass
