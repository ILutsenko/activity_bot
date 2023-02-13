FROM python:3.10

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
COPY ./app.py .
RUN pip install -r requirements.txt
COPY . .
