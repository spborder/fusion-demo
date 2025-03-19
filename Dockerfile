FROM python:3.11

RUN pip install fusion-tools[interactive]==3.5.5

ENV DSA_URL "https://3-230-122-132.nip.io/api/v1"
ENV APP_PORT 8050

EXPOSE 8050
COPY ./app.py app.py
CMD ["python","app.py"]