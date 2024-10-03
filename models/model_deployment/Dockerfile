# create dockerfile  instructions for creating an image
# docker run -it --rm python:3.8.12-slim                        run python in docker
# docker run -it --rm --entrypoint=bash python:3.8.12-slim      run bash in docker
# type exit to exit
# by running bash commands you can run python code, install packages, ..

# base image
FROM python:3.8.12-slim
RUN pip install pipenv

RUN pip install scikit-learn
# create a directory and go there
WORKDIR /app
# copy the file to current directory "./"
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --system --deploy
COPY ["predict.py", "model_C=1.0.bin", "./"]
# docker build -t zoomcamp-test . # docker fiel from current directory, define tag with -t

# docker run -it --rm --entrypoint=bash zoomcamp-test

# docker is already isolated no need to create a virtual env using RUN install pipenv 
# but need to tell to install librarieds to sys environemtn


# gunicorn --bind=0.0.0.0:9696 predict:app
# python -m waitress --listen=0.0.0.0:9696 predict:app
# install packages 
# run comand to build docker image
# run the docker image

## packages


## port

