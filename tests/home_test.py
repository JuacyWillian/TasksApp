import unittest

from kivy.clock import Clock

from tasks import TasksApp
from tasks.screens import SCREENS_TYPE
from tasks.screens.home_screen import HomeScreen
from tasks.screens.task_edit_screen import TaskEditScreen


class HomeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = TasksApp()
        Clock.schedule_once(lambda *x: self.app.stop(), 0.000001)
        self.app.run()

        self.toolbar = self.app.root.ids.toolbar

    def test_home_type(self, ):
        screen = self.app.root.ids.manager.current_screen
        self.assertIsInstance(screen, HomeScreen)

    def test_home_screen_name(self, ):
        screen = self.app.root.ids.manager.current
        self.assertEqual(screen, 'home')

    def test_toolbar_title(self,):
        self.assertEqual(self.toolbar.title, 'Tasks')

    def test_toolbar_right_action_items(self, ):
        r_items = self.toolbar.right_action_items
        self.assertEqual(len(r_items), 2)

    def test_plus_button_on_toolbar(self, ):
        btn = self.__get_toolbar_button('plus')
        self.assertIsNotNone(btn)

    def __get_toolbar_button(self, icon):
        right_actions = self.toolbar.ids.right_actions.children
        for btn in right_actions:
            if btn.icon == icon:
                return btn

    def test_plus_button_action(self, ):
        plus_btn = self.__get_toolbar_button('plus')
        plus_btn.dispatch('on_release')
        screen = self.app.root.ids.manager.current
        self.assertEqual(screen, 'new_task')

    def test_about_button_action(self, ):
        btn = self.__get_toolbar_button('information-outline')
        btn.dispatch('on_release')
        screen = self.app.root.ids.manager.current
        self.assertEqual(screen, 'about')

    def test_info_button_on_toolbar(self, ):
        btn = self.__get_toolbar_button('information-outline')
        self.assertIsNotNone(btn)


class HomeToolbarTestCase(unittest.TestCase):
    pass


class TaskListTestCase(unittest.TestCase):
    pass
