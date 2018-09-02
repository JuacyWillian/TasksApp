from kivymd.toolbar import Toolbar

__toolbar = Toolbar()

def get_toolbar():
    if not __toolbar:
        global __toolbar
        __toolbar = Toolbar()
    return __toolbar
