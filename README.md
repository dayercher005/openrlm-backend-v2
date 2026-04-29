# Backend Service for openrlm
Backend Server for openrlm desktop application

### Start Development Environment

Prerequisite

- Python

Install Dependencies
```bash
pip install sqlmodel "fastapi[standard]" openrlm alembic sqlalchemy
```

Setting up environment variables
```bash
# Either "openrouter" or "anthropic"
RLM_PROVIDER=

# Type of AI Model (e.g claude-sonnet-4.5)
AI_MODEL=

# If using paid OpenRouter API Key
OPENROUTER_API_KEY=

# If using paid Anthropic API Key
ANTHROPIC_API_KEY=

# Frontend URL (for CORS)
FRONTEND_URL=

# PostgreSQL details
PG_USER=
PG_PASSWORD=
PG_HOST=
PG_PORT=
PG_DATABASE=
```

Run Development Server
```bash
fastapi dev
```