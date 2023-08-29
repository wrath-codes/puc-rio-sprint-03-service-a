# flake8: noqa: F401

from src.models import Child, Parent

from .db_base import Base
from .db_config import DBConnectionHandler


def database_setup():
    """Create database tables and relationships."""

    db_conn = DBConnectionHandler()
    engine = db_conn.get_engine()

    Base.metadata.create_all(engine)
