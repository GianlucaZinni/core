from fastapi import FastAPI
from votechain_core.stacks.votestamp import VotestampStack


class Core:
    def __init__(self, app: FastAPI):
        # Initialize the application
        self.app = app

        self.votestamp = VotestampStack(app)
