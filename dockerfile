FROM python:3.8.0-alpine

RUN apk add --no-cache python3-dev \ 
    && pip3 install --upgrade pip

WORKDIR /app
COPY . /app 
RUN pip3 --no-cache install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["shortner.py"]


