from schemas.schema import reservation, room
from models.model import Room, Reservation


class HotelService():

    def __init__(self, db) -> None:
        self.db = db


    def get_rooms(self):
        return self.db.query(room).all()


    def get_rooms_available(self, available):
        return self.db.query(room).filter(room.available == available).all()


    def create_room(self, room: Room):
        new_room = Room(**room.dic())
        self.db.add(new_room)
        self.db.commit()
        return


    def update_room(self, room_id, available):
        room_upd = self.db.query(room).filter(room.id == room_id).first()
        room_upd.available = available
        self.db.commit()
        return


    def delete_room(self, room_id):
        self.db.query(room).filter(room.id == room_id).first().delete()
        self.db.commit()
        return
