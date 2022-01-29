FROM python:3.10.2-alpine

WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/

EXPOSE 8000 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
