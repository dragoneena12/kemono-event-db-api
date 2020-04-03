# lapi-house-program-api

## 参考
- Django REST Frameworkでユーザ認証周りのAPIを作る
https://qiita.com/xKxAxKx/items/60e8fb93d6bbeebcf065

## 課題
- Generic viewsがよくわかってない
- エンドポイントがばらばらなの直したい
- debugを外すとおかしくなる

## やること
`settings_secret.py` を環境に応じて作成する。

```
docker-compose up -d
docker-compose exec web bash
python manage.py migrate
```

localで開発するときは http://10.65.80.76:8000/admin で接続