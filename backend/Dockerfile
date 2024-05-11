FROM python:3.11-alpine

WORKDIR /backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "8000"]