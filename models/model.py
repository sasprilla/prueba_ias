
from config.database import Base
from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey, DateTime, String


class Floor(Base):
    __tablename__ = 'floors'

    id = Column(Integer, primary_key=True)
    floor = Column(Integer)


class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    floor_id = Column(Integer, ForeignKey(floor.id))
    available = Column(Boolean)
    night_value = Column(Float)
    number_guests = Column(Integer)


class Guest(Base):
    __tablename__ = 'guest'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    document_type = Column(String)
    document_number = Column(Integer)


class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey(room.id))
    entry_date = Column(DateTime,)
    departure_date = Column(DateTime,)
    guest_id = Column(Integer, ForeignKey(guest.id))
