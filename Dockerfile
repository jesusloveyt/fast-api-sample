FROM python:3.11.9

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 88

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "88"]