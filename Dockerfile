FROM python:3.8.0
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 80
CMD gunicorn --bind 0.0.0.0:80 app:app
