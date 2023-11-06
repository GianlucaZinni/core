from fastapi import FastAPI
from layers.database.sqlalchemy.index import SQLAlchemyHandler
from layers.resources import IntegratorResources


class SchedulerStack:
    def __init__(self, app: FastAPI = None):
        # Access to the parameters resources
        resources = IntegratorResources()   

        self.app = app



votestamp = SchedulerStack()
