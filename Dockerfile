FROM python:3.8.0

ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

ENV PORT=80

ENV DB_NAME='IReNEdb'
ENV DB_HOST="mongodb://testuser:testpassword@irene-db:27017/?authSource=admin"

ENV GOOGLE_OAUTH_CLIENT_ID=125759116505-flugvdnnv7lm6q6htj62uic5ut70e594.apps.googleusercontent.com

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 80
CMD gunicorn --bind 0.0.0.0:80 app:app
