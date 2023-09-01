# flake8: noqa: F401
from src.models import *

from .db_base import Base
from .db_config import DBConnectionHandler


def create_db():
    """Creates a database if it does not exist"""

    db_conn = DBConnectionHandler()
    engine = db_conn.get_engine()

    Base.metadata.create_all(engine)
