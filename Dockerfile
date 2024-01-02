FROM python:3.12

WORKDIR /usr/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./assets ./assets

ENV PYTHONPATH=/usr/app/src

CMD [ "python", "src/main.py" ]
