from flask import Flask
from job_manager import JobManager
from job_manager.jobs import ManagerProcess, teste


app = Flask(__name__)
app.secret_key = "secret"
jm = JobManager(app)


manager_process = jm.tasks
processo1 = manager_process.new(
    "teste1",
    teste,
    group="Ola Mundo",
    description="uma task de teste para visualização",
)
processo2 = manager_process.new(
    "teste2",
    teste,
    description="uma task de teste para visualização",
)
processo3 = manager_process.new(
    "teste3",
    teste,
    description="uma task de teste para visualização",
)
processo4 = manager_process.new(
    "teste4",
    teste,
)
