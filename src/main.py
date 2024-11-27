from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.status import HTTP_401_UNAUTHORIZED

from .back import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # create db tables here
    yield

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    title='Dyumium',
    version="1.0",
    middleware=[
        Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
    ],
    lifespan=lifespan)

app.include_router(router)
