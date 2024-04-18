FROM python:3.9.19-bookworm
WORKDIR /usr/src/Trembita
COPY . /usr/src/Trembita
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]
