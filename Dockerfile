# ベースイメージの指定
FROM python:3.11.9

# アプリケーションの作業ディレクトリを設定
WORKDIR /app

# アプリケーションのソースコードをコンテナにコピー
COPY . /app

# 必要なパッケージをインストール
RUN pip install -r requirements.txt

# コンテナ起動時に実行されるコマンド
CMD ["python", "src/main.py"]
