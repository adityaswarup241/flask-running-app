# A simple Flask app container.
FROM python:3-buster
LABEL maintainer="Aditya Swarup"

EXPOSE 5000
# Place app in container.
COPY . /opt/www
WORKDIR /opt/www

# Install dependencies.
RUN pip install -r requirements.txt

EXPOSE 80
CMD python web.py

