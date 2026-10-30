FROM  python:3.12.3-slim-bookworm
RUN apt-get update && \ 
apt-get upgrade -y && \
rm -rf /var/lib/apt/lists/*
LABEL Description="SafeRelease Project"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python","app/app.py" ]
