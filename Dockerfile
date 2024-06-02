FROM python:3.9.19-bookworm
WORKDIR /usr/src/Trembita
COPY . /usr/src/Trembita
RUN pip install -r requirements.txt
EXPOSE 80
CMD uvicorn trembita.main:app --reload --host 0.0.0.0 --port 80
