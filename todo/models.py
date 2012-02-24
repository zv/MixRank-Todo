from sqlalchemy import (
    Column,
    Integer,
    Text,
    Boolean,
    String
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    order = Column(Integer)
    done = Column(Boolean)

    def __init__(self, content, done, order):
        self.content = content
        self.done = done

    def to_json(self):
        return """{id: %s, content: "%s", order: %s, done: %s}""" % (self.id, self.content, self.order, self.done)
    def to_dictionary(self):
        return {"id" : self.id, "content" : self.content, "order" : self.order, "done" : self.done}

