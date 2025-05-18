
FROM python:3.12-slim AS builder
RUN pip install poetry==1.8.4

ENV POETRY_VIRTUALENVS_IN_PROJECT=1
ENV POETRY_VIRTUALENVS_CREATE=1
ENV POETRY_CACHE_DIR=/tmp/poetry_cache



ARG DEBIAN_FRONTEND=noninteractive

RUN echo 'Acquire::http::Timeout "30";\nAcquire::http::ConnectionAttemptDelayMsec "2000";\nAcquire::https::Timeout "30";\nAcquire::https::ConnectionAttemptDelayMsec "2000";\nAcquire::ftp::Timeout "30";\nAcquire::ftp::ConnectionAttemptDelayMsec "2000";\nAcquire::Retries "15";' > /etc/apt/apt.conf.d/99timeout_and_retries      && apt-get update      && apt-get -y dist-upgrade      && apt-get -y install gcc
RUN mkdir /app
COPY . /app/





RUN cd /app && poetry install --no-interaction --no-ansi 

FROM python:3.12-slim AS runtime

LABEL org.opencontainers.image.title=finduz
LABEL org.opencontainers.image.version=0.1.0
LABEL org.opencontainers.image.authors=['Javakhir Shavkatov <zshavkatov51@gmail.com>']
LABEL org.opencontainers.image.licenses=
LABEL org.opencontainers.image.url=
LABEL org.opencontainers.image.source=

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1


WORKDIR /app
COPY --from=builder /app/ /app/
ENV PYTHONPATH="${PYTHONPATH}:/app"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]