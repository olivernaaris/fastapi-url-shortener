# Run app with restart
uvicorn app.main:app --reload

# URL-s
http://127.0.0.1:8000
http://127.0.0.1:8000/docs

# Example requests
## Get
# Welcome message
curl http://127.0.0.1:8000

# List all Url-s in db
curl http://127.0.0.1:8000/list

# Get original Url from short Url
curl http://127.0.0.1:8000/35QwBDQH

## Post
# Create short Url
curl -X POST http://127.0.0.1:8000/shorten -H "accept: application/json" -H  "Content-Type: application/json" -d "{\"url\":\"https://youtube.com\"}"
