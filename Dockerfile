# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk update && apk add --no-cache bash
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY . ./

# Install API dependencies
RUN pipenv install

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]