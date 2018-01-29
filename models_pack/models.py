from peewee import *
from playhouse.migrate import *
from playhouse.fields import *
from datetime import datetime

import models_pack

db = SqliteDatabase('vneurokabot.db')
migrator = SqliteMigrator(db)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_name = CharField()
    user_surname = CharField()
    user_id = IntegerField()
    user_level = IntegerField(default=0)
    user_start_game = DateTimeField(null=True)
    user_end_game = DateTimeField(null=True)


class Task(BaseModel):
    task_text = TextField()
    task_right_answer = TextField()
    task_photo = BlobField(null=True)
    task_file = BlobField(null=True)


# TODO: дописать связи для моделей

class Category(BaseModel):
    category_task = ManyToManyField(Task, related_name='tasks')
    category_name = CharField()
    task_winner = ForeignKeyField(User)


ListCategory = Category.category_task.get_through_model()
