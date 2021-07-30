FROM python:3
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

WORKDIR /app

COPY . . 
RUN pip install -r requirements.txt

ENTRYPOINT [ "sh", "entrypoint.sh" ]
