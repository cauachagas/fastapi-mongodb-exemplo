FROM python:3.8.8-alpine3.13

MAINTAINER Cauã Chagas "caua.geof@gmail.com"

# set working directory
WORKDIR /usr/src/

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# Não copiará os arquivos em .dockerignore
COPY . .

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Script que facilita a iniciaização do servidor na porta $PORT
COPY start.sh .

RUN chmod +x start.sh

# run the command
CMD ["./start.sh"]
