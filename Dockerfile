# Dockerfile

FROM python:3.11-slim

WORKDIR /app

RUN apt update && apt -y upgrade && apt -y dist-upgrade && apt -y autoremove && apt -y autoclean
RUN apt -y install \
    sudo \
    curl \
    git \
    vim \
    nano \
    sudo \
    build-essential \
    tree

RUN pip install --upgrade pip && \
    pip install poetry

RUN poetry config virtualenvs.create false

# 環境変数の設定ファイルをコピー
COPY .env .

# Poetryで必要な依存関係をインストール
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
