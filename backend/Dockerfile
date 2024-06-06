FROM python:3.11.6

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir --user -r requirements.txt

# Run the backend server
ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
