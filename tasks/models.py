from datetime import datetime

from kivy.event import EventDispatcher
from kivy.properties import *


class Task(EventDispatcher):
    title = StringProperty('')
    body = StringProperty('')
    finished = BooleanProperty(False)
    date = ObjectProperty(None)
    tag = StringProperty('')

    __tasks = []

    @classmethod
    def getAll(cls, ):
        return cls.__tasks

    @classmethod
    def getById(cls, id: int):
        return cls.__tasks[id]

    @classmethod
    def insert(cls, task):
        cls.__tasks.append(task)

    @classmethod
    def update(cls, id: int, task):
        cls.__tasks = [t for t in cls.__tasks if cls.__tasks.index(t) != id]

    @classmethod
    def remove(cls, id: int):
        cls.__tasks.remove(id)

    def __init__(self, title, body, **kwargs):
        super(Task, self).__init__()
        self.title = title
        self.body = body
        self.status = kwargs.get('finished', False)
        self.date = kwargs.get('date', datetime.now())
        self.tag = kwargs.get('tag', '')

    def on_title(self, instance, value):
        print(f'new title: {value}')

    def on_body(self, instance, value):
        print(f'new title: {value}')

    def on_status(self, instance, value):
        print(f'new status: {value}')

    def on_date(self, instance, value):
        print(f'new date: {value}')

    def on_tag(self, instance, value):
        print(f'new tag: {value}')

    def __str__(self):
        return f'{self.title}'


task_list = [
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
    Task('Pagar a conta de luz', 'preciso pagar a conta de luz antes do dia 15'),
]
