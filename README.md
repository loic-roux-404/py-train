# Cours basés sur python

### Install windows

```ps1
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
puis :

```bash
choco install -y miniconda3 --params="'/AddToPath:1'" --force
```

### Install mac

- `brew install miniconda`

### Then

- Add more packages channels : `conda config --add channels conda-forge`
- Create env :
```sh
cd advanced-algo && conda create -y --name $(basename "$PWD") python=3.7 --file requirements.txt
```

- Launch : `conda activate op-research`
- Switch python interpreter to this env on Vscode bottom left
- To stop venv : `conda deactivate`

> For more on conda : [Here the cheatseet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

### Scripting
1. [Matplot lib](https://mmas.github.io/conics-matplotlib)
