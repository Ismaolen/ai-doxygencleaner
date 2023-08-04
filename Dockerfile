# Use the latest version of Alpine Linux
FROM alpine:latest

# Update the package list
# RUN apk update

# Install Python3, Doxygen, pip, and other dependencies
RUN apk add --no-cache python3 doxygen py3-pip python3-dev mariadb-dev build-base npm git curl

# Install Python packages
RUN pip3 install pygments openai tiktoken python-dotenv mysqlclient rich

# Install Node.js packages
RUN npm install -g diff2html-cli

# Clean up
RUN rm -rf /var/cache/apk/*
