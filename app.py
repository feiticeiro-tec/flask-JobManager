from flask import Flask
from job_manager import JobManager
from job_manager.jobs import ManagerProcess, teste


app = Flask(__name__)
app.secret_key = "secret"
jm = JobManager(app)

processo1 = jm.tasks.new(
    "teste1",
    teste,
    group="Ola Mundo",
    description="uma task de teste para visualização",
)
processo2 = jm.tasks.new(
    "teste2",
    teste,
    description="uma task de teste para visualização",
)
processo3 = jm.tasks.new(
    "teste3",
    teste,
    description="uma task de teste para visualização",
)
processo4 = jm.tasks.new(
    "teste4",
    teste,
)