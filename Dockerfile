FROM python:3.6-slim

RUN pip install flask gunicorn

WORKDIR /app

ADD . .
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "--reload", "app:app"]
#CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload

