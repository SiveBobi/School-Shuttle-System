from typing import Optional, List
from repositories.reservation_repository import ReservationRepository
from src.reservation import Reservation

class InMemoryReservationRepository(ReservationRepository):
    def __init__(self):
        self._storage = {}

    def save(self, reservation: Reservation) -> None:
        self._storage[reservation.reservation_id] = reservation

    def find_by_id(self, reservation_id: str) -> Optional[Reservation]:
        return self._storage.get(reservation_id)

    def find_all(self) -> List[Reservation]:
        return list(self._storage.values())

    def delete(self, reservation_id: str) -> None:
        if reservation_id in self._storage:
            del self._storage[reservation_id]
