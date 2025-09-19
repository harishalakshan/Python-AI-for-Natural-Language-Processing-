FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m nltk.downloader punkt stopwords wordnet

EXPOSE 5000

CMD ["python", "src/main.py"]
