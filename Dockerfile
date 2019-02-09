FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
ENV FLASK_DEBUG false
ENV FLASK_APP /code/app

WORKDIR /code
COPY /architecture /code

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt

ENTRYPOINT flask run -h 0.0.0.0 -p 8000
