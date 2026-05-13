from importlib.metadata import PackageNotFoundError, version

from .constants.types import StateType
from .manager import Manager
from .models.task_model import TaskModel

try:
    __version__ = version("propel")
except PackageNotFoundError:  # package not installed
    __version__ = "0.0.0+unknown"

__all__ = [
    "Manager",
    "StateType",
    "TaskModel",
    "__version__",
]
