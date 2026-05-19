# --- builder stage ---
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN pip install --no-cache-dir uv

WORKDIR /app
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev || uv sync --no-dev

# --- runtime stage ---
FROM python:3.12-slim AS runtime

LABEL org.opencontainers.image.title=finduz
LABEL org.opencontainers.image.version=0.1.0
LABEL org.opencontainers.image.authors="Javakhir Shavkatov <zshavkatov51@gmail.com>"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH="/app"

# non-root runtime user
RUN groupadd --system app && useradd --system --gid app --create-home --home /home/app app

WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY --chown=app:app . /app/

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD python -c "import urllib.request, sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/api/schema/', timeout=3).status < 500 else 1)"

# Run migrations then start uvicorn. Use a stable SECRET_KEY in env at deploy time.
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && exec uvicorn core.asgi:application --host 0.0.0.0 --port 8000"]
