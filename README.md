# Cours basés sur python

1. [Algorithmique avancée et structures de données](#Algo)

1. [IA et recherche opérationnelle](#AI)

# Algo
> **Algorithmique avancée et structures de données**

#### 0. Requis

- `python 3.x`

#### 1. Introduction : algorithmes

- Organigrammes (losange pour représenter une condition)
- Suite de syracuse
- scratch (algo GUI)
- Q# --> simulation des proc quantiques

#### 2. Python

- haut niveau
- structure de données évoluée : ensembles, listes, dict,...
- open source / beaucoup de documentation

1. Debug

- Coeff binomial `python advanced-algo/intro.py`
- Coeff binomial `python advanced-algo/recursions/simple.py`
- Tri fusion `python advanced-algo/recursions/mergeSort.py`

## Env

- `conda` package manager recommanded (installed over miniconda)

# AI
> Ia et recherche opérationnelle

## Install

- Required `conda` package manager [(download windows)](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
- Add more packages channels : `conda config --add channels conda-forge`
- Create env :
```sh
conda create -y --name op-research python=3.7 --file op-research/requirements.txt
```

- Launch : `conda activate op-research`
- Switch python interpreter to this env on Vscode bottom left
- (Optional) Jupyter notebook : `jupyter notebook --generate-config`
- To stop venv : `conda deactivate`

> For more on conda : [Here the cheatseet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## Courses

1. [Introduction RO & IA](doc/op-research/intro.md)
1. [Programmation linéaire](doc/op-research/linear-prog-simplexes.md)

### Scripting
1. [Matplot lib](https://mmas.github.io/conics-matplotlib)
