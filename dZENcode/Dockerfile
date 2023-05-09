FROM python:3.11.0

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PUTHONUNBUFFERED 1
ENV ENVIRONMENT 'local'

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/requirements.txt

RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/dZENcode

WORKDIR /usr/src/dZENcode

EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
