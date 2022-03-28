FROM python:3.8-slim-buster

WORKDIR /app
RUN apt update && apt install sqlite3 && apt autoclean
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

COPY . .

RUN pip3 install .
EXPOSE 5000 
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
