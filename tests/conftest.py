from datetime import datetime

import pytest

from propel.manager import Manager
from propel.models.task_model import TaskModel


@pytest.fixture(scope="function")
def task() -> TaskModel:
    return TaskModel(
        title="Test Task",
        description="Test Description",
        expiration_date=datetime(2026, 12, 31),
    )


@pytest.fixture(scope="function")
def manager() -> Manager:
    return Manager()


@pytest.fixture(scope="function")
def manager_with_task(manager: Manager, task: TaskModel) -> Manager:
    manager.add_task(task=task)
    return manager
