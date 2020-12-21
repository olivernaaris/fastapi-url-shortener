# Run app with restart
uvicorn app.main:app --reload

# URL-s
http://127.0.0.1:8000
http://127.0.0.1:8000/docs

# Example requests
## Get
curl http://127.0.0.1:8000
curl http://127.0.0.1:8000/list
## Post
curl -X POST http://127.0.0.1:8000/shorten -H "accept: application/json" -H  "Content-Type: application/json" -d "{\"url\":\"https://youtube.com\"}"# fastapi-url-shortener
