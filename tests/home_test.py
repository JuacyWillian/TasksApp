import unittest

from kivy.clock import Clock

from tasks import TasksApp
from tasks.screens.home_screen import HomeScreen


class HomeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = TasksApp()
        Clock.schedule_once(lambda *x: self.app.stop(), 0.000001)
        self.app.run()

        self.toolbar = self.app.root.ids.toolbar


    def test_home_type(self, ):
        self.assertIsInstance(self.app.root.ids.manager.current_screen, HomeScreen)

    def test_home_screen_name(self, ):
        self.assertEqual(self.app.root.ids.manager.current, 'home')

    def test_toolbar_right_action_items(self, ):
        self.assertEqual(len(self.toolbar.right_action_items), 2)

    def test_plus_button_on_toolbar(self, ):
        self.assertIsNotNone(self.__get_toolbar_button('plus'))

    def __get_toolbar_button(self, icon):
        right_actions = self.toolbar.ids.right_actions.children
        for btn in right_actions:
            if btn.icon == icon:
                return btn

    def test_plus_button_action(self, ):
        self.__get_toolbar_button('plus').dispatch('on_release')
        self.assertEqual(self.app.root.ids.manager.current, 'new_task')

    def test_about_button_action(self, ):
        self.__get_toolbar_button('information-outline').dispatch('on_release')
        self.assertEqual(self.app.root.ids.manager.current, 'about')

    def test_info_button_on_toolbar(self, ):
        self.assertIsNotNone(self.__get_toolbar_button('information-outline'))


class HomeToolbarTestCase(unittest.TestCase):
    pass


class TaskListTestCase(unittest.TestCase):
    pass
