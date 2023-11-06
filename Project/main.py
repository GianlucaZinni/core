import os
import sys

# Construye la ruta al directorio raíz del proyecto
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Añade la ruta del directorio raíz del proyecto al sys.path
sys.path.append(PROJECT_DIR)

# Crea las bases de datos
from layers.database.mysql.create_databases import create_databases

create_databases()

import uvicorn
from votechain_core import create_app


votechain_app = create_app()

# from apscheduler.schedulers.background import BackgroundScheduler
# from Project.votechain_core.stacks.scheduler.functions.schedule.index import (
#     function
# )
from layers.resources import IntegratorResources

resources = IntegratorResources()

# sched = BackgroundScheduler(deamon=True)
# sched.add_job(function, "interval", seconds=resources.params["SCHEDULE"]["INTERVAL"])
# sched.start()

if __name__ == '__main__':
    uvicorn.run("main:votechain_app", host='0.0.0.0', port=8000)