from .repository import Repository
from src.reservation import Reservation

class ReservationRepository(Repository[Reservation, str]):
    """Reservation Repository extends the generic Repository for Reservation objects."""
    pass
