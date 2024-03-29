FROM python:3

WORKDIR /usr/src/app

EXPOSE 80

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
