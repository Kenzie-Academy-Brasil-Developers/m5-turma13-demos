FROM python:3.11.0-alpine

# Não utilizar os arquivos .pyc na construção da imagem
ENV PYTHONDONTWRITEBYTECODE 1

# Os logs de erro não se percam no buffer de texto do terminal
ENV PYTHONUNBUFFERED 1

WORKDIR /django_project

COPY . /django_project/

RUN pip install -U pip
RUN pip install -r requirements.txt
# Só usando o sqlite3
# RUN python manage.py migrate

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]