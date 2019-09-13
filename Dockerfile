FROM python:3.6.5-alpine3.7

#MAINTANER Your Name "youremail@domain.tld"


# We copy just the requirements.txt first to leverage Docker cache

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt


RUN pip install -r requirements.txt

COPY . /app
#ENTRYPOINT [ "python" ]
ENV FLASK_APP=server/__init__.py

CMD [  "python", "app.py" ]