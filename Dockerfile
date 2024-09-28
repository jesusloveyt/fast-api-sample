FROM python:3.11.9

COPY ./app /app
COPY requirements.txt requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 88

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "88"]