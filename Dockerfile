FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir -p /usr/src/chbt
WORKDIR /usr/src/chbt

ENV PORT=5000

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD uvicorn --host 0.0.0.0 --port $PORT bot:app