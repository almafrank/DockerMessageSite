FROM python:3.10-alpine

WORKDIR /app  #Man kan skriva /code också så kopierar man allt i mappen

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app  #Man kan lägga till COPY . .

EXPOSE 5001

CMD ["python3","app.py"]