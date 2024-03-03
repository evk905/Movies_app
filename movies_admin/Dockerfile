FROM python:3.10

WORKDIR /opt/app
#RUN groupadd -r docker && useradd -m -d /opt/app -r -g docker myuser \
#    && chown -R myuser:docker /opt/app && chmod 777 /opt/app -R


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'


COPY run_uwsgi.sh /opt/app/run_uwsgi.sh
COPY ../requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini /opt/app/uwsgi.ini

RUN  pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . /opt/app/

EXPOSE 8000
#USER myuser:docker

CMD ["uwsgi", "--strict", "--ini", "uwsgi.ini"]