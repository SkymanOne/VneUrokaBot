from playhouse.migrate import *
from playhouse.fields import *
from models_pack.models import *

db.create_tables([
        User,
        Task,
        Category,
        ListCategory])
