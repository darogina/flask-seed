# Using lightweight alpine image
FROM python:3.6-alpine
ENV PYTHONUNBUFFERED=1

# Installing packages
RUN apk update && apk add --no-cache bash build-base
RUN set -ex && pip install --no-cache-dir pipenv --upgrade

# Defining working directory and adding source code
WORKDIR /app
COPY . ./

# Install API dependencies
RUN pipenv install --deploy

# Start app
EXPOSE 5000
ENTRYPOINT ["/app/bootstrap.sh", "-w"]