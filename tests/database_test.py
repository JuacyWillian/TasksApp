import unittest
from kivy.clock import Clock
from tasks import TasksApp


class DatabaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = TasksApp()
        Clock.schedule_interval(lambda *x: self.app.stop(), 0.000001)
        self.app.run()
