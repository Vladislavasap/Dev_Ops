FROM python:3.7-slim

WORKDIR /app

COPY yamdb_final/ /app

RUN pip3 install -r /app/api_yamdb/requirements.txt --no-cache-dir

CMD gunicorn api_yamdb.api_yamdb.wsgi:application --bind 0:8000 

#CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]