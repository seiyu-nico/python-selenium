FROM python:3.7
# 環境変数 PYTHONUNBUFFEREDを設定
ENV PYTHONUNBUFFERED 1
# mkdirコマンドの実行
# 作業ディレクトリの設定
WORKDIR /app
COPY requirements.txt ./
# Pythonのパッケージ管理ツールのpipをアップグレード
RUN pip install --upgrade pip
# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install -r requirements.txt

ENV user tech
RUN useradd -u 1000 -m -d /home/${user} -g staff ${user} \
     && chown -R ${user} /home/${user}
USER ${user}