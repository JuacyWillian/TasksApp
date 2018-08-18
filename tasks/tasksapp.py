from kivy.app import App
from kivy.core.window import Window
from kivy.properties import *
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.elevationbehavior import RectangularElevationBehavior
from kivymd.label import MDLabel
from kivymd.list import (ILeftBody, IRightBodyTouch, MDList, OneLineListItem,
                         TwoLineIconListItem)
from kivymd.navigationdrawer import NavigationDrawerHeaderBase
from kivymd.theming import ThemableBehavior, ThemeManager

from tasks.models import Task, task_list


class NavigationDrawerHeader(RelativeLayout, ThemableBehavior, RectangularElevationBehavior, NavigationDrawerHeaderBase):
    title = StringProperty()
    title_color = ListProperty([1, 1, 1, 1])

    subtitle = StringProperty('')
    subtitle_color = ListProperty([1, 1, 1, 1])

    source = StringProperty('data/navHeader_bg.jpg')
    avatar = StringProperty('')
    avatar_circle_color = ListProperty([1, 1, 1, 1])

    def __init__(self, **kw):
        super().__init__(**kw)
        self.title = App.get_running_app().get_application_name()
        self.subtitle = 'juacy.willian@gmail.com'


class MDIcon(MDLabel):
    icon = StringProperty('')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.font_style: 'Icon'

    def on_icon(self, instance, value):
        self.text: u"{}".format(md_icons[root.icon])
        return True


class IconLeftSampleWidget(ILeftBody, MDIconButton):
    def __init__(self, task, **kwargs):
        super().__init__(**kwargs)

        self.icon = f"checkbox-{'marked' if task.finished else 'blank'}-outline"


class IconRightSampleWidget(IRightBodyTouch, MDIconButton):
    pass


class TaskListItem(TwoLineIconListItem):
    def __init__(self, task: Task, **kwargs):
        super().__init__(**kwargs)
        self.text = task.title
        self.secondary_text = f"{task.date}\t{task.tag}"
        self.add_widget(IconLeftSampleWidget(task))


class NewTaskDialog(MDDialog):
    datepicker = ObjectProperty(None)

    def show_date_picker(self,):
        self.datepicker = MDDatePicker(self.set_previous_date)
        self.datepicker.open()

    def set_previous_date(self, date):
        text_date = self.ids.task_date
        text_date.text = str(date)
        self.datepicker.dismiss()


class TaskList(MDList):
    def __init__(self, items, **kwargs):
        super().__init__(**kwargs)
        for i in items:
            self.add_task(i)

    def add_task(self, task):
        self.add_widget(TaskListItem(task))


class HomeScreen(Screen):
    tasks_list = ListProperty([])
    tasks = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

    def on_tasks_list(self, *args):
        self.load_tasks()

    def on_enter(self,):
        scroll = ScrollView(do_scroll_x=False)
        self.tasks = TaskList([], id='taskList')

        self.tasks_list = Task.getAll()
        scroll.add_widget(self.tasks)
        self.add_widget(scroll)

    def load_tasks(self, ):
        if self.tasks:
            self.tasks.clear_widgets()
            for t in self.tasks_list:
                self.tasks.add_task(t)

    def show_new_task_dialog(self, *args):
        dialog = NewTaskDialog()
        dialog.add_action_button("Dismiss", lambda *x: dialog.dismiss())
        dialog.add_action_button("Create", lambda *x: self.create_task(dialog))
        dialog.open()

    def create_task(self, dialog):
        self.tasks_list.append(
            Task(
                dialog.ids.task_name.text,
                dialog.ids.task_body.text,
                finished=dialog.ids.task_finished.active,
                date=dialog.ids.task_date.text,
                tag=dialog.ids.task_tag.text
            )
        )
        dialog.dismiss()


class TaskEditScreen(Screen):
    def on_pre_enter(self, *args):
        super().on_pre_enter(*args)

    def on_enter(self, *args):
        super().on_enter(*args)

    def on_pre_leave(self, *args):
        super().on_pre_leave(*args)

    def on_leave(self, *args):
        super().on_leave(*args)


class TasksApp(App):
    """Basic kivy app

    Edit tasks.kv to get started.
    """
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Teal'

    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        return self.root

    def on_request_close(self, *args):
        # print('request close')
        # return True
        pass

    def on_stop(self, ):
        print('on stop')
