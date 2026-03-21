from datetime import datetime

import pytest

from task_manager.manager import Manager
from task_manager.models.task_model import TaskModel


@pytest.fixture
def expiration_date() -> datetime:
    return datetime(year=2025, month=12, day=31)


@pytest.fixture
def task(expiration_date: datetime) -> TaskModel:
    return TaskModel(
        title="Test Task",
        description="Test Description",
        expiration_date=expiration_date,
    )


@pytest.fixture
def manager() -> Manager:
    return Manager()


@pytest.fixture
def manager_with_task(manager: Manager, task: TaskModel) -> Manager:
    manager.add_task(task=task)
    return manager
