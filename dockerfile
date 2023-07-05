# python:3.8の公式 image をベースの image として設定
FROM python:3.10.11

COPY requirements.txt .
# pipアップグレード
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt
# 作業ディレクトリの作成
RUN mkdir /mysite

# 作業ディレクトリの設定（以後の RUN は WORKDIR で実行）
WORKDIR /mysite

# カレントディレクトリにある資産をコンテナ上の指定のディレクトリにコピーする
ADD ../djangoAI /mysite