FROM python:3.11-slim-buster AS builder

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./requirements.txt ./
RUN python -m pip install -r requirements.txt \
    && apt-get update && apt-get install wget -y

FROM python:3.11-slim-buster  AS runner

COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /usr/bin/wget /usr/bin/wget
COPY --from=builder /usr/lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/
ENV PATH="/opt/venv/bin:$PATH"
COPY ./src ./app/src
COPY ./main.py ./app/
WORKDIR /app

ENTRYPOINT ["python", "main.py"]