# Arm requirements (Mac)

Install conda :

```
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh
rm -rf Mambaforge-$(uname)-$(uname -m).sh

conda init $SHELL
```

`conda env create -f environment.yml`
`pip install -r requirements.mac.txt`

# Classic x64 requirements (Linux)

`conda env create dl`
`pip install -r requirements.txt` (not tested)
