FROM python:3.9.19-bookworm
WORKDIR /usr/src/Trembita
COPY . /usr/src/Trembita
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python manage.py && flask run --host=0.0.0.0
