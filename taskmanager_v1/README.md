# DjangoでCeleryを使って非同期処理をするためのサンプル

# Dockerの環境構築

```bash
docker network create tm-network
docker docker volume create pgdata
```

```bash
# ビルド
docker-compose build
# 起動
docker-compose up
```

```bash
# マイグレーションの実行
docker-compose run server python3 manage.py migrate
# 管理ユーザーの作成
docker-compose run server python3 manage.py createsuperuser
```


# Celeryのコマンド


**schedulerの起動**

```bash
DJANGO_SETTINGS_MODULE=tm.settings celery -b beat

DJANGO_SETTINGS_MODULE=tm.settings celery beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

**workerの起動**

```bash
DJANGO_SETTINGS_MODULE=tm.settings celery -A tapp_a worker
```


# コマンド

ユーザーの追加

```bash
python3 manage.py createsuperuser
```

マイグレーションの実行

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```


プロジョクトの作成

```bash
django-admin startproject [project name]
```

アプリの追加

```bash
python3 manage.py startapp [app name]
```

ライブラリのインストール

```bash
pip3 install -r requirements.txt
```