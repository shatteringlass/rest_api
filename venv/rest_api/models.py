from datetime import date
from datetime import datetime
#from uuid import UUID, uuid4
from pony.orm import *


db = Database()


class Couple(db.Entity):
    id = PrimaryKey(int, auto=True)
    effdate = Optional(datetime)
    messages = Set('Message')
    user_couple = Optional('UserCouple')
    couple_scores = Set('CoupleScore')
    couple_day = Optional('CoupleDay')


class Emoji(db.Entity):
    id = PrimaryKey(int, auto=True)
    text = Required(str)
    descr = Optional(str)
    score = Optional(int)
    emoji_msgs = Set('EmojiMsg')


class Message(db.Entity):
    id = PrimaryKey(int, auto=True)
    timestamp = Required(datetime, default=lambda: datetime.now())
    emoji_msgs = Optional('EmojiMsg')
    sender = Required('User')
    couple = Required(Couple)
    status = Required(str, default='ready')
    couple_day = Optional('CoupleDay')


class UserScore(db.Entity):
    id = PrimaryKey(str)
    user = Required('User')
    value = Optional(str)
    timestamp = Optional(str)


class CoupleScore(db.Entity):
    id = PrimaryKey(str)
    couple = Required(Couple)
    value = Optional(str)
    timestamp = Optional(str)


class User(db.Entity):
    login = Required('Login')
    msg = Set(Message)
    user_scores = Set(UserScore)
    user_couple = Optional('UserCouple')


class UserCouple(db.Entity):
    id = PrimaryKey(int, auto=True)
    couple = Required(Couple)
    user = Required(User)


class EmojiMsg(db.Entity):
    id = PrimaryKey(int, auto=True)
    emoji = Required(Emoji)
    message = Required(Message)


class Login(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Optional(User)
    nickname = Required(str)
    password = Required(str)
    email = Optional(str)
    regdate = Required(datetime, default=lambda: datetime.now())
    lastlog = Optional(datetime)


class Day(db.Entity):
    date = PrimaryKey(date, default=lambda: date.today())
    couple_day = Optional('CoupleDay')


class CoupleDay(db.Entity):
    id = PrimaryKey(int, auto=True)
    day = Required(Day)
    message = Required(Message)
    couple = Required(Couple)