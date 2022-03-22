try:
    from Vortex.plugins.sql_helper import SESSION, BASE
except ImportError:
    raise Exception("Hello!")

from sqlalchemy import Column, String


class GMute(BASE):
    __tablename__ = "gmute"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


GMute.__table__.create(checkfirst=True)


def is_gmuted(sender_id):
    try:
        return SESSION.query(GMute).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def gmute(sender):
    adder = GMute(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def ungmute(sender):
    rem = SESSION.query(GMute).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def all_gmuted():
    rem = SESSION.query(GMute).all()
    SESSION.close()
    return rem

# SQL 
class GM(BASE):
    __tablename__ = "sgmute"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


GM.__table__.create(checkfirst=True)


def fukkk(sender_id):
    try:
        return SESSION.query(GM).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def gmt(sender):
    add = GM(str(sender))
    SESSION.add(add)
    SESSION.commit()


def ungmt(sender):
    if riz := SESSION.query(GM).get((str(sender))):
        SESSION.delete(riz)
        SESSION.commit()
