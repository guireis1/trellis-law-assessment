from typing import List

from fastapi import Depends, FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api import router
from core import config
from core.exceptions import CustomException
from core.fastapi import Logging


def on_auth_error(request: Request, exc: Exception):
    """
    Handles authentication errors.

    Args:
        request (Request): The request object.
        exc (Exception): The exception object.

    Returns:
        JSONResponse: The JSON response containing the error code and message.
    """
    status_code, error_code, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        error_code = exc.error_code
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content={"error_code": error_code, "message": message},
    )


def init_routers(app_: FastAPI) -> None:
    """
    Initializes the routers for the FastAPI application.

    Args:
        app_ (FastAPI): The FastAPI application instance.
    """
    app_.include_router(router)


def init_listeners(app_: FastAPI) -> None:
    """
    Initializes the exception handler for CustomException.

    Args:
        app_ (FastAPI): The FastAPI application instance.
    """
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def make_middleware() -> List[Middleware]:
    """
    Creates and returns the list of middleware for the FastAPI application.

    Returns:
        List[Middleware]: The list of middleware.
    """
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
    return middleware


def create_app() -> FastAPI:
    """
    Creates and configures the FastAPI application.

    Returns:
        FastAPI: The configured FastAPI application instance.
    """
    app_ = FastAPI(
        title=config.APP_NAME,
        description=config.APP_DESCRIPTION,
        version=config.APP_VERSION,
        debug=config.DEBUG,
        docs_url=None if config.ENVIRONMENT == "production" else "/docs",
        redoc_url=None if config.ENVIRONMENT == "production" else "/redoc",
        dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)

    return app_


app = create_app()
