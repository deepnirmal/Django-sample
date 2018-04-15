FROM frolvlad/alpine-python3

ADD requirements.txt  /requirements.txt
RUN python3 -m pip
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

RUN mkdir /code/
WORKDIR /code/
ADD . /code/

EXPOSE 8000

RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput

#CMD python3 manage.py runserver




