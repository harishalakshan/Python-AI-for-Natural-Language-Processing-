# Python AI for Natural Language Processing (NLP)

## Overview
This project demonstrates a Python-based NLP system with AI capabilities such as:

- Text preprocessing (tokenization, stopword removal, lemmatization)
- Sentiment analysis
- Basic text classification
- Dockerized deployment for easy setup

## Requirements
- Python 3.9+
- Docker (for containerized deployment)

## Installation
```bash
git clone <repo_url>
cd python-ai-nlp
pip install -r requirements.txt
```

## Usage
```bash
python src/main.py
```

## Docker Deployment
```bash
docker build -t python-ai-nlp .
docker run -it --rm python-ai-nlp
```

## Project Structure
- `src/` : Source code (preprocessing, models, main execution)
- `data/` : Sample text files
- `models/` : Saved ML/NLP models
- `Dockerfile` : Docker setup for deployment
