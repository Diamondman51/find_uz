FROM python:3.12-slim

ADD . /app

WORKDIR /app

RUN pip install uv

# RUN uv sync --locked
COPY . .
RUN uv sync

CMD ["uv", "run", "uvicorn", "core.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
# EXPOSE 8000

# COPY requirements.txt ./

# RUN pip install --no-cache-dir -r requirements.txt

# # RUN uv venv /opt/venv
# # ENV VIRTUAL_ENV=/opt/venv
# # ENV PATH="/opt/venv/bin:$PATH"
# # RUN uv venv
# # RUN uv sync


# # CMD ["python", "-m", "uvicorn", "core.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
