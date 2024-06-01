FROM python:3.9.19-bookworm
WORKDIR /usr/src/Trembita
COPY . /usr/src/Trembita
RUN pip install -r requirements.txt
EXPOSE 8000
CMD uvicorn trembita.main:app --reload
