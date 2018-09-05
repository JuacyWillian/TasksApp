from peewee import *

db = SqliteDatabase('data/database/tasks.db')


class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    name = CharField()
    birthday = DateField()


class Task(BaseModel):
    title = CharField()
    date = DateField()
    finished = BooleanField()
    tag = CharField()


table_list = [Task, Person]