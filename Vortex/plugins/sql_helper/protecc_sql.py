

from sqlalchemy import Boolean, Column, Integer, String as STRING_SESSION, UnicodeText
from Vortex.plugins.sql_helper import SESSION, BASE



class Harem(BASE):
    __tablename__ = "harem"
    chat_id = Column(STRING_SESSION(14), primary_key=True)
    
    def __init__(self, chat_id):
        self.chat_id = chat_id


Harem.__table__.create(checkfirst=True)


def add_grp(chat_id: str):
    waifu = Harem(str(chat_id))
    STRING_SESSION.add(waifu)
    STRING_SESSION.commit()


def rm_grp(chat_id: str):
    if waifu := STRING_SESSION.query(Harem).get(chat_id):
        STRING_SESSION.delete(waifu)
        STRING_SESSION.commit()


def get_all_grp():
    waifu = STRING_SESSION.query(Harem).all()
    STRING_SESSION.close()
    return waifu


def is_harem(chat_id: str):
    try:
        if waifu := STRING_SESSION.query(Harem).get(chat_id):
            return str(waifu.chat_id)
    finally:
        STRING_SESSION.close()
