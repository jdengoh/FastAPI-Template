# FastAPI-Template

A FastAPI template for my experimental learning

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![uv](https://img.shields.io/badge/uv-DE5FE9?style=for-the-badge&logo=astral&logoColor=white)](https://docs.astral.sh/uv/)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
  - [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Backend Setup](#backend-setup)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Running backend with Script](#running-backend-with-script)
  - [Running backend with Docker](#running-backend-with-docker)
  - [Running with Uvicorn](#running-with-uvicorn)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Development](#development)
- [Contributors](#contributors)
- [License](#license)

## Overview <a id="overview"></a>

TODO: Overview

## Features <a id="features"></a>

TODO: Features

## Project Structure <a id="project-structure"></a>

### Folder Structure <a id="folder-structure"></a>

```sh
app/
  api/            # FastAPI routers and endpoints
  core/           # Core config, environment, logging
  database/       # Database models and enums
  schemas/        # Global schemas for API and cross-agent use
  services/       # Service layer (agent orchestration, auth, etc.)
  config/         # Logging and app config
scripts/          # Startup and utility scripts
Dockerfile        # Docker build
README.md         # Its THE readme you are reading!
```

## Getting Started <a id="getting-started"></a>

### Prerequisites <a id="prerequisites"></a>

- [Python 3.13 or higher](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package and project manager

## Backend Setup <a id="backend-setup"></a>

### Create a Virtual Environment <a id="create-a-virtual-environment"></a>

This project uses `uv` as the Python package and project manager.

Create the venv:

```sh
uv venv
```

Activate the venv.

On macOS or Linux, run:

```sh
source .venv/bin/activate
```

On Windows, run:

```powershell
.venv/Scripts/activate
```

Install project dependencies:

```sh
uv sync
```

### Running backend with Script <a id="running-backend-with-script"></a>

On macOS or Linux, run:

```sh
./scripts/start.sh
```

On Windows, run:

```ps1
./scripts/start.ps1
```

### Running backend with Docker <a id="running-backend-with-docker"></a>

*NOTE: docker only runs for the backend, frontend has to be ran separately*

On macOS or Linux, run:

```sh
./scripts/start_docker.sh
```

On Windows, run:

```ps1
./scripts/start_docker.ps1
```

### Running with Uvicorn <a id="running-with-uvicorn"></a>

Run the following command to run the app with Uvicorn:

```sh
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

## Environment Variables <a id="environment-variables"></a>

**Backend environemtn variables**: Copy `.env.example` to `.env` in the project root and fill in all required fields:

```env
FRONTEND_HOST=http://localhost:3000
BACKEND_CORS_ORIGINS=http://localhost:8000
```

- Replace `your-key` with your actual API keys.
- These variables are required for both backend and frontend integration.
- Never commit your real `.env` file to version control.

## API Endpoints <a id="api-endpoints"></a>

| Endpoint | Method | Description |
|----------|--------|-------------|

## Development <a id="development"></a>

TODO: Development Notes

## Contributors <a id="contributors"></a>

TODO: List contributors

## License

MIT
