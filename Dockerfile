# Pull base image
FROM python:3.10.2-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .





#WORKDIR /usr/src/app/"${BOT_NAME:-tg_bot}"

#COPY requirements.txt /usr/src/app/"${BOT_NAME:-tg_bot}"
#RUN pip install -r /usr/src/app/"${BOT_NAME:-tg_bot}"/requirements.txt
#COPY . /usr/src/app/"${BOT_NAME:-tg_bot}"




