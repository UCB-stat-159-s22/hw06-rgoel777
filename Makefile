.PHONY: env
env:
    mamba env create -f environment.yml

.PHONY: html
html:
    jupyterbook build .

.PHONY: html-hub
html-hub:
    cd hw06rgoel777
    jupyter-book config sphinx .
    sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
    cd _build/html
    python -m http.server

.PHONY: clean:
clean:
    rm -f figures/*.png
    rm -f audio/*wav
    rm -rf _build
    rm -rf hw06rgoel777/_build