from fastapi import FastAPI
from layers.database.sqlalchemy.index import SQLAlchemyHandler
from layers.resources import IntegratorResources


class VotestampStack:
    def __init__(self, app: FastAPI = None):
        # Access to the parameters resources
        self.sqlalchemy = SQLAlchemyHandler()
        self.integrator_resources = IntegratorResources()   
        self.db_session = self.sqlalchemy.connect("VOTESTAMP")


def sql_add(db_session, register):
    db_session.add(register)
    db_session.commit()


def sql_delete(db_session, register):
    db_session.delete(register)
    db_session.commit()


votestamp = VotestampStack()
