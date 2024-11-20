import uvicorn
from fastapi import FastAPI
from app.api.v1.endpoints.user import router as api_router
app = FastAPI()

app.include_router(api_router,prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app")