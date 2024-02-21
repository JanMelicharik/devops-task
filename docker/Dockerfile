FROM python:3.11.8

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app/

ENTRYPOINT [ "uvicorn", "bookstore.main:app", "--host", "0.0.0.0", "--port", "8000" ]