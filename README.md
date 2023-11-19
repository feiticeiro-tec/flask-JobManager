# Flask JobManager

Biblioteca de gerenciamento de tarefas, ao definir uma tarefa sera catalogado em uma lista de tarefas e poderar ser visto em uma pagina web.

a biblioteca ta em teste e abertas a contribuições.

## Como implementar
a definição da secret_key é importante para o uso, na falta da definição da variavel JOB_MANAGER_PASSWORD_KEY a secret_key sera usada como senha para acessar os jobs

```python
app = Flask(__name__)
jm = JobManager(app)
```
ou

```python
app = Flask(__name__)
jm = JobManager()
jm.init_app(app)
```

## Como criar uma task

```python

# definição da tarefa
def teste():
    ...

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

```

## Tela de gerenciamento
