FROM python:3.12-alpine3.23

COPY ./realbpo/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./realbpo /app/

CMD ["python","/app/manage.py","runserver","0.0.0.0:8000"]