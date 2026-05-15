# Backend Service for openrlm
Backend Server for openrlm desktop application

---
## Project Structure

```bash
.
├── alembic.ini
├── compose.yaml
├── Dockerfile
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── pyproject.toml
├── README.Docker.md
├── README.md
├── requirements.txt
└── src
    ├── app.py
    ├── config.py
    ├── libs
    │   └── database.py
    ├── middleware
    ├── models
    │   ├── __init__.py
    │   ├── conversation.py
    │   ├── message.py
    │   └── models.py
    ├── routers
    │   ├── conversation_list.py
    │   ├── conversation.py
    │   └── new_conversation.py
    ├── schemas
    │   ├── __init__.py
    │   ├── conversation.py
    │   └── message.py
    └── services
        └── rlm_engine.py
```

---

## Development

### Prerequisite
- Python
- Docker


### Setup Environment
- Create a local .env file:
```bash
cp .env.example .env
```
You can find the required environment variables in `.env.example`.

### Start Development Environment
- Build and start the app server and database:
```bash
docker compose up --build
```

- Run database migration:
```bash
docker compose exec run alembic upgrade head
```

- View consolidated logs:
```bash
docker compose logs -f
```

- Shutdown the app server and database:
```bash
docker compose down
```

### Local URLs

FastAPI Server:
```bash
http://localhost:8000/
```

API Reference: 
```bash
http://localhost:8000/docs
```

Postgres DB host port:
```bash
5432
```

## API Documentation & Endpoints

| Method   | Endpoint                        | Description                         |
| -------- | ------------------------------- | ----------------------------------- |
| GET      | /conversations                  | Get list of all conversations       |
| GET/POST | /new-conversation               | Create new conversation             |
| GET/POST | /conversations/{conversationId} | Get individual conversation         |
