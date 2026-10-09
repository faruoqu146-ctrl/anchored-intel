from datetime import datetime, timedelta, timezone
from typing import Optional, Literal
import os
import hashlib
import hmac
import secrets
import time
import json
import math
from collections import defaultdict

from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from pydantic import BaseModel, Field, model_validator

try:
    from google.oauth2 import id_token as google_id_token
    from google.auth.transport import requests as google_requests
except Exception:
    google_id_token = None
    google_requests = None

import httpx
from sqlalchemy import create_engine, String, Float, DateTime, ForeignKey, Text, Boolean, Integer, select, UniqueConstraint, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, sessionmaker

APP_VERSION = "1.7.1"
BUILD_VERSION = APP_VERSION
INTELLIGENCE_MODEL_VERSION = "iei-0.1"
# NOTE: Full file restored in next steps if truncated - applying critical check-in fix
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./nexgene.db")
DEV_MODE = os.getenv("DEV_MODE", "false").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY") or "nexgene-local-development-secret-only"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(bind=engine)

app = FastAPI(title="NexGene API", version=APP_VERSION)

@app.get("/health")
def health():
    return {"status": "ok", "note": "Partial restore - full main.py needs re-upload"}
