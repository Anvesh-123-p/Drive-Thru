FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip3 install --upgrade pip wheel
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code/
EXPOSE 8080
CMD python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8080 --noreload
