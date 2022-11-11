FROM python:3.10

WORKDIR /app

COPY Pipfile* /app/

RUN pip install pipenv

RUN pipenv requirements > requirements.txt

RUN pip install -r requirements.txt

COPY * /app/
