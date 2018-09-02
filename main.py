
try:
    import kivy
    kivy.require('1.10.1')

    from tasks.tasksapp import tasks_app

    if __name__ == "__main__":
        tasks_app.run()

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
