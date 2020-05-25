FROM python:3.8-alpine
RUN apk update
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD myservice /myservice
ENV PORT 5000
ENV WORKERS 4
CMD gunicorn -w ${WORKERS} -b :${PORT} myservice.service:app
