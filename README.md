# Backend Service for openrlm
Backend Server for openrlm desktop application


### Start Development Environment

Prerequisite

- Python

Install Dependencies
```bash
pip install sqlmodel "fastapi[standard]"
```

Setting up environment variables
```bash
OPENROUTER_API_KEY= # For paid Open Router API Key

ANTHROPIC_API_KEY= # For paid Anthropic API Key
```

Run Development Server
```bash
fastapi dev
```