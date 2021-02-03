# DS Algo

> **Algorithmique avancée et structures de données**

#### 0. Requis

- `python 3.x`

## Env

- `conda` package manager recommanded (installed over miniconda)

## Install

- Required `conda` package manager [(download windows)](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
- Add more packages channels : `conda config --add channels conda-forge`
- Create env :
```sh
conda create -y --name op-research python=3.7 --file src/requirements.txt
```

## Start jupyter

- `conda activate op-research`
- `cd src/ && jupyter notebook`

## TDD

- Enable with this line on top `from tests import run`
- Use with `run()` function :

Voilà comment faire :

```py
# Import du module python
from tests import run

def syracuse(start, query, sequence = []):
    # Ici le code fonctionnel requis par l'exercice
    pass

# Arg 1 : Fonction sans les arguments
# Arg 2, Un dictionnaire / objet python avec comme structure :
# - Une clé "args" qui contient un autre dict avec les arguments passés dans la fonction,
#   ces clés du dict (ex "start": 14) doivent avoir exactement le même nom que
#   les arguments de la fonction
# - Une clé "result" qui doit être le résultat renvoyer par la fonction
run(syracuse, [
    {'args': {'start': 14, 'query': 5}, 'result': 34},
    {'args': {'start': 14, 'query': 2}, 'result': 7},
    {'args': {'start': 14, 'query': 1}, 'result': 14},
])

```
