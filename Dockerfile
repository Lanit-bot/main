# Install base Python image
FROM python:3.8-slim-buster

# Copy files to the container
COPY *.py /app/
COPY requirements.txt /app/
COPY *.csv /app/
COPY questionary-2.json /app/

# Set working directory to previously added app directory
WORKDIR /app/

# Install dependencies
RUN apt-get install g++

RUN pip install -r requirements.txt
RUN apt-get install gzip
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install wget -y

EXPOSE 80

CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
