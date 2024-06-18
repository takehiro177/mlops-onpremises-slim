FROM python:3.8

RUN pip install "feast[redis,postgres]"

COPY ./feature_store.yaml feature_store.yaml

ENV FEAST_USAGE=False

CMD ["feast", "serve", "-h", "0.0.0.0"]