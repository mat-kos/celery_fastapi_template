FROM python:3.11-slim-buster AS builder

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./requirements.txt ./
RUN python -m pip install -r requirements.txt

FROM python:3.11-slim-buster  AS runner

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./src ./app/src
COPY ./main.py ./app/
WORKDIR /app
RUN mkdir -p /var/run/celery /var/log/celery \
    && chown -R nobody:nogroup /var/run/celery /var/log/celery
ENV DOCKER_CELERY_UID=nobody
ENV DOCKER_CELERY_GID=nogroup

ENTRYPOINT ["python", "main.py"]