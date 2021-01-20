FROM python:alpine
ADD requirements.txt /
RUN apk update --no-cache \
  && apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps \
  && pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r /requirements.txt \
  && apk del .build-deps
RUN apk add postgresql-libs  --no-cache