import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import platform as p


Base = declarative_base()


class Note(Base):

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    note_body = Column(String)
    created_at = Column(String, default=datetime.datetime.now())
    posted_by = Column(String, default=p.uname().node)

    def __repr__(self):
        return f'Note(id={self.id}, title={self.title}, note_body={self.note_body}), posted_by={self.posted_by} ,created_at={self.created_at})'



