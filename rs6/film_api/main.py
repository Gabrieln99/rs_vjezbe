from fastapi import FastAPI
from routers.filmovi import router as filmovi_router

app = FastAPI(
    title="RS6 Film API",
    description="FastAPI mikroservis za filmove"
)

app.include_router(filmovi_router)
