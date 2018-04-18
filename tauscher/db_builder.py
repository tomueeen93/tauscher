# -*- coding: utf-8 -*-

import os

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from base import Base

def create_tables(db_route):
    """
    Creates the table objects
    :param db_route:
    :return:
    """
    engine = create_engine('postgresql://{0}'.format(db_route))

    Base.Base.metadata.bind = engine
    Base.Base.metadata.create_all(engine)

    insp = inspect(engine)  # will be a PGInspector
    print(insp.get_enums())

def make_session(db_route):
    """
    Create a session for interfacing with the postgres DB.
    :param db_route: user:password@url/puckmath string
    :return: session, engine
    """

    engine = create_engine('sqlite://{0}'.format(db_route))

    Base.Base.metadata.bind = engine
    Base.Base.metadata.create_all(engine)

    _session = sessionmaker(bind=engine)
    session = _session()

    return session, engine


if __name__ == '__main__':
    puckmath_url = os.environ['CONFIG_PATH']
    session, engine = make_session(db_route=db_route)
