FROM vm/ubuntu:18.04

RUN apt-get update && apt-get install python3.8 python3-pip

COPY . .
RUN pip3 install poetry==1.1.4 && poetry install
CHECKPOINT disabled

SECRET ENV ptt_id_1
SECRET ENV ptt_id_2
SECRET ENV bot_token
SECRET ENV chat_id

RUN poetry run python main.py
