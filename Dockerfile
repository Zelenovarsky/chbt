FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir -p /usr/src/chbt
WORKDIR /usr/src/chbt

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

