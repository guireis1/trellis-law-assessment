from enum import Enum

from starlette.config import Config
from starlette.datastructures import Secret


class EnvironmentType(str, Enum):
    """
    Enumeration class representing different environment types.
    """
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"
    
config = Config(".env")

APP_NAME: str = "Number to English"
APP_VERSION: str = "0.1"
APP_DESCRIPTION: str = "Project assessment for Trellis Law"
API_KEY: Secret = config("API_KEY", cast=Secret)
DEBUG: int = 0
DEFAULT_LOCALE: str = "en_US"
ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
