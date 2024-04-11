import uvicorn

from core.config import ENVIRONMENT

if __name__ == "__main__":
    uvicorn.run(
        app="core.server:app",
        reload=True if ENVIRONMENT != "production" else False,
        workers=1,
    )
