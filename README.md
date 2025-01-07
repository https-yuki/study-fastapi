# study-fastapi
FastAPIの勉強用

## ローカル環境開発手順
```
# コンテナの起動
docker compose up -d

# fastapiコンテナに入る
docker exec -it fastapi bash

# マイグレーションを実行
alembic upgrade head

# テスト実行
pytest tests
```

## その他
```
# API仕様書
http://localhost:8000/docs

# コンテナの停止とボリュームの削除
docker compose down --volumes
```
