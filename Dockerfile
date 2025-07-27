FROM python:3.13-alpine

ENV HLDS_ADDRESS=0.0.0.0
ENV HLDS_PORT=27000

RUN apk add --no-cache curl

WORKDIR /app
COPY . .
RUN pip install uv && uv sync

EXPOSE ${HLDS_PORT}

HEALTHCHECK --interval=1m --timeout=3s CMD curl -f http://localhost:${HLDS_PORT}/ping || exit 1

ENTRYPOINT ["sh", "-c", "uv run gunicorn --bind ${HLDS_ADDRESS}:${HLDS_PORT} app:app"]
