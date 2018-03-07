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

