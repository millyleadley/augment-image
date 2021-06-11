FROM amd64/python:3.9.5-slim AS base
# working directory in the container; following a conventional directory layout
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

# earlier stage allows us to only partially build the Dockerfile when just testing
FROM base as test
RUN pip install -r requirements.dev.txt
RUN pytest

FROM base as prod
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000
# TODO: remove
ENV FLASK_ENV=development
CMD ["flask", "run"]