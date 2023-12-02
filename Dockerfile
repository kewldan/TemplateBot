FROM python:3.12

WORKDIR /usr/app
COPY requirements.txt ./
RUN pip install -r --no-cache-dir requirements.txt

COPY ./src ./src
COPY ./assets ./assets

ENV PYTHONPATH=/usr/app/src

CMD [ "python", "src/main.py" ]
