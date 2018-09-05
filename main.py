from tasks import TasksApp
try:
    import kivy
    kivy.require('1.10.1')

    if __name__ == "__main__":
        TasksApp().run()

except Exception as ex:
    import logging
    import traceback
    import sys

    logger = logging.getLogger('tasks')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('tasks.log', mode='w')
    fh.setLevel(logging.ERROR)
    logger.addHandler(fh)

    logger.log(logging.ERROR, traceback.format_exc())
