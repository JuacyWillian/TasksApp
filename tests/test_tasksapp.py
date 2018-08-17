#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from tasks.tasksapp import TasksApp


class TestTasksApp(unittest.TestCase):
    """TestCase for TasksApp.
    """
    def setUp(self):
        self.app = TasksApp()

    def test_name(self):
        self.assertEqual(self.app.name, 'tasks')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
