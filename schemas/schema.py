from pydantic  import BaseModel, Field
from datetime import datetime,
from typing import Optional, Required, 

class floor(BaseModel):
    __tablename__ = 'floors'

    id: Optional[int] = None
    floor : int 


class room(BaseModel):

    id = Column(Integer, primary_key=True)
    # floor_id = Column(Integer, ForeignKey(floor.id))
    available : bool 
    night_value : float
    number_guests : int


class guest(BaseModel):
    __tablename__ = 'guest'

    id: Optional[int] = None
    name: str = Field(max_length=30, pattern=r'/^([^0-9]*)$/')
    document_type: str
    document_number: int = Field(max_length=12)


class reservation(BaseModel):

    id: Optional[int] = None
    # room_id = Column(Integer, ForeignKey(room.id))
    entry_date: datetime = Field(str='dd/mm/yyyy HH:mm:ss')
    departure_date: datetime = Field(str='dd/mm/yyyy HH:mm:ss')
