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

## Tela de gerenciamento
