FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . .

RUN ln -sf /app/migrate_db.sh /usr/bin/migrate_db.sh

#ADD https://www.postgresql.org/media/keys/ACCC4CF8.asc ./
#RUN apt-key add ACCC4CF8.asc

#RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN DEBIAN=noninteractive apt-get update && apt-get install -y postgresql-client-13 vim

#RUN python manage.py makemigrations

#RUN python manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
