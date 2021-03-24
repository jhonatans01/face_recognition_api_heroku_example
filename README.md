# Face recognition app with Dlib + Flask + Heroku + Docker

This project is a basic example of face recognition using Dlib library, which provides machine learning algorithms. In
this example, we use Python 3.6, Dlib 19.21.1 and Flask 1.1.2.

## Run locally with Docker

```bash
docker-compose up --build
```

## Run locally with Conda

In the conda environment that you created for the project, there are 2 main dependencies to install.

```bash
conda install -c conda-forge dlib
conda install -c conda-forge opencv
```

## Run locally with virtualenv

To run with virtualenv, you need to install some dependencies:

- [Boost](https://www.boost.org/)
- [Boost.Python](https://www.boost.org/doc/libs/1_57_0/libs/python/doc/index.html)
- [Cmake](https://cmake.org/)
- [X11/XQuartx](https://www.xquartz.org/)

After that, you need to create the virtual environment and install the dependencies.

```bash
python -m venv .
```

For Linux / OSX

```bash
# for linux / OSX
source myproject/bin/activate

#for windows
myproject\Scripts\activate
```

```bash
pip install -r requirements.txt
```

