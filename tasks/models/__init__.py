# coding= utf-8
import os

from peewee import BooleanField, CharField, DateField, Model, SqliteDatabase

database_uri = os.environ.get('DATABASE_URI', 'tasks.db')
db = SqliteDatabase(database_uri)


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


def init_db():
    with db:
        db.create_tables(table_list)
