FROM python:3.11

RUN useradd --create-home films
WORKDIR /films

COPY requirements.txt requirements-dev.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install -r requirements-dev.txt

COPY . .

RUN chown films:films ./

USER films

EXPOSE 5000

CMD ["python", "./wsgi.py"]
