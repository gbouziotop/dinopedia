FROM python:3.10.2-slim

ARG USER_ID
ARG GROUP_ID

COPY requirements/requirements.txt .

RUN apt-get -yq update

RUN python3 -m pip install --upgrade pip setuptools pip-tools

RUN python3 -m pip install -r requirements.txt

WORKDIR /usr/dinopedia/app

RUN /bin/bash -c 'if [ ${USER_ID} ]; then addgroup --gid ${GROUP_ID} appuser && useradd -r -u ${USER_ID} -g ${GROUP_ID} appuser | chpasswd && adduser appuser sudo | chown -R appuser:appuser /usr/dinopedia/app; else useradd -r appuser ; fi'