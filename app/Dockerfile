FROM amd64/python:3.9.5-slim

WORKDIR /usr/src/app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000
# TODO: remove
ENV FLASK_ENV=development

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]