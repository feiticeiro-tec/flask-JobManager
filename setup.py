from setuptools import setup


import os


def listar_subpastas(diretorio):
    subpastas = [diretorio]
    for nome in os.listdir(diretorio):
        caminho = os.path.join(diretorio, nome)
        if os.path.isdir(caminho):
            subpastas.append(caminho)
            subpastas.extend(listar_subpastas(caminho))
    return subpastas


with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name="flask-job_manager",
    version="0.1.0",
    url="https://github.com/feiticeiro-tec/feiticeiro-tec",
    license="BSD3",
    author="Silvio Henrique Cruz Da Silva",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="silviohenriquecruzdasilva@gmail.com",
    keywords="python, feiticeiro-tec, flask",
    description=("pacote de gerenciamento de jobs para flask"),
    packages=listar_subpastas("job_manager"),
    install_requires=["loguru"],
)
