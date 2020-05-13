# kemono-event-db-api
## やること
`settings_secret.py` を環境に応じて作成する。

```
docker-compose up -d
docker-compose exec web bash
python manage.py migrate
```

localで開発するときは http://10.65.80.76:8000/admin で接続