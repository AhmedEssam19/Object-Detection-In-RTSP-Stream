FROM ultralytics/ultralytics:8.1.18

COPY . /home/app

WORKDIR /home/app

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "app:app", "--backlog", "100", "-b", "0.0.0.0",  "--workers", "1", "--timeout", "3600"]