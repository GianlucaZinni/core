from fastapi import FastAPI
from votechain_core.config import Config
from votechain_core.stacks import Core
from dotenv import load_dotenv


def create_app(config_class=Config):
    load_dotenv()
    # Flask app object
    app = FastAPI()
    app.config = config_class

    # Configuring from Python Files
    Core(app)
    
    from votechain_core.stacks.votestamp.functions.voteregister.routes import voteregister
    
    app.include_router(voteregister)
    
    return app
