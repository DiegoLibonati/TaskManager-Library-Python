from collections.abc import KeysView, ValuesView
from datetime import datetime

import pytest

from propel.manager import Manager
from propel.models.task_model import TaskModel
from propel.utils.exceptions import ConflictError, NotFoundError, ValidationError


class TestManagerInit:
    @pytest.mark.unit
    def test_initial_tasks_is_empty_dict(self, manager: Manager) -> None:
        assert manager.tasks == {}

    @pytest.mark.unit
    def test_initial_len_tasks_is_zero(self, manager: Manager) -> None:
        assert manager.len_tasks == 0

    @pytest.mark.unit
    def test_tasks_keys_is_keys_view(self, manager: Manager) -> None:
        assert isinstance(manager.tasks_keys, KeysView)

    @pytest.mark.unit
    def test_tasks_values_is_values_view(self, manager: Manager) -> None:
        assert isinstance(manager.tasks_values, ValuesView)


class TestManagerAddTask:
    @pytest.mark.unit
    def test_add_task_increases_len(self, manager: Manager, task: TaskModel) -> None:
        manager.add_task(task=task)
        assert manager.len_tasks == 1

    @pytest.mark.unit
    def test_add_task_stores_task_by_id(self, manager: Manager, task: TaskModel) -> None:
        manager.add_task(task=task)
        assert task.id in manager.tasks_keys

    @pytest.mark.unit
    def test_add_task_stores_correct_task_instance(self, manager: Manager, task: TaskModel) -> None:
        manager.add_task(task=task)
        assert manager.tasks[task.id] is task

    @pytest.mark.unit
    def test_add_multiple_tasks(self, manager: Manager) -> None:
        task1: TaskModel = TaskModel(title="Task 1", description="Desc 1", expiration_date=datetime(2026, 12, 31))
        task2: TaskModel = TaskModel(title="Task 2", description="Desc 2", expiration_date=datetime(2026, 12, 31))
        manager.add_task(task=task1)
        manager.add_task(task=task2)
        assert manager.len_tasks == 2

    @pytest.mark.unit
    def test_add_non_task_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.add_task(task="not a task")  # type: ignore[arg-type]

    @pytest.mark.unit
    def test_add_non_task_error_has_correct_code(self, manager: Manager) -> None:
        with pytest.raises(ValidationError) as exc_info:
            manager.add_task(task=42)  # type: ignore[arg-type]
        assert exc_info.value.code == "NOT_VALID_TASK"

    @pytest.mark.unit
    def test_add_duplicate_task_raises_conflict_error(self, manager: Manager, task: TaskModel) -> None:
        manager.add_task(task=task)
        with pytest.raises(ConflictError):
            manager.add_task(task=task)

    @pytest.mark.unit
    def test_add_duplicate_task_error_has_correct_code(self, manager: Manager, task: TaskModel) -> None:
        manager.add_task(task=task)
        with pytest.raises(ConflictError) as exc_info:
            manager.add_task(task=task)
        assert exc_info.value.code == "ALREADY_EXISTS_TASK"


class TestManagerRemoveTask:
    @pytest.mark.unit
    def test_remove_task_decreases_len(self, manager_with_task: Manager, task: TaskModel) -> None:
        manager_with_task.remove_task(id_task=task.id)
        assert manager_with_task.len_tasks == 0

    @pytest.mark.unit
    def test_remove_task_removes_from_dict(self, manager_with_task: Manager, task: TaskModel) -> None:
        manager_with_task.remove_task(id_task=task.id)
        assert task.id not in manager_with_task.tasks_keys

    @pytest.mark.unit
    def test_remove_empty_id_raises_validation_error(self, manager_with_task: Manager) -> None:
        with pytest.raises(ValidationError):
            manager_with_task.remove_task(id_task="")

    @pytest.mark.unit
    def test_remove_nonexistent_id_raises_not_found_error(self, manager: Manager) -> None:
        nonexistent_task: TaskModel = TaskModel(title="Ghost", description="Ghost", expiration_date=datetime(2026, 1, 1))
        with pytest.raises(NotFoundError):
            manager.remove_task(id_task=nonexistent_task.id)

    @pytest.mark.unit
    def test_remove_nonexistent_error_has_correct_code(self, manager: Manager) -> None:
        nonexistent_task: TaskModel = TaskModel(title="Ghost", description="Ghost", expiration_date=datetime(2026, 1, 1))
        with pytest.raises(NotFoundError) as exc_info:
            manager.remove_task(id_task=nonexistent_task.id)
        assert exc_info.value.code == "NOT_FOUND_TASK"


class TestManagerEditTask:
    @pytest.mark.unit
    def test_edit_task_title(self, manager_with_task: Manager, task: TaskModel) -> None:
        manager_with_task.edit_task(id_task=task.id, title="Updated Title")
        assert task.title == "Updated Title"

    @pytest.mark.unit
    def test_edit_task_description(self, manager_with_task: Manager, task: TaskModel) -> None:
        manager_with_task.edit_task(id_task=task.id, description="Updated Description")
        assert task.description == "Updated Description"

    @pytest.mark.unit
    def test_edit_task_expiration_date(self, manager_with_task: Manager, task: TaskModel) -> None:
        new_date: datetime = datetime(2027, 6, 15)
        manager_with_task.edit_task(id_task=task.id, expiration_date=new_date)
        assert task.expiration_date == new_date

    @pytest.mark.unit
    def test_edit_task_empty_id_raises_validation_error(self, manager_with_task: Manager) -> None:
        with pytest.raises(ValidationError):
            manager_with_task.edit_task(id_task="", title="New")

    @pytest.mark.unit
    def test_edit_task_nonexistent_id_raises_not_found_error(self, manager: Manager) -> None:
        ghost_task: TaskModel = TaskModel(title="Ghost", description="Ghost", expiration_date=datetime(2026, 1, 1))
        with pytest.raises(NotFoundError):
            manager.edit_task(id_task=ghost_task.id, title="New")


class TestManagerMoveTaskByState:
    @pytest.mark.unit
    def test_move_task_to_in_progress(self, manager_with_task: Manager, task: TaskModel) -> None:
        manager_with_task.move_task_by_state(id_task=task.id, state="in_progress")
        assert task.state == "in_progress"

    @pytest.mark.unit
    def test_move_task_to_complete(self, manager_with_task: Manager, task: TaskModel) -> None:
        manager_with_task.move_task_by_state(id_task=task.id, state="complete")
        assert task.state == "complete"

    @pytest.mark.unit
    def test_move_task_empty_id_raises_validation_error(self, manager_with_task: Manager) -> None:
        with pytest.raises(ValidationError):
            manager_with_task.move_task_by_state(id_task="", state="in_progress")

    @pytest.mark.unit
    def test_move_task_nonexistent_id_raises_not_found_error(self, manager: Manager) -> None:
        ghost_task: TaskModel = TaskModel(title="Ghost", description="Ghost", expiration_date=datetime(2026, 1, 1))
        with pytest.raises(NotFoundError):
            manager.move_task_by_state(id_task=ghost_task.id, state="in_progress")

    @pytest.mark.unit
    def test_move_task_invalid_state_raises_validation_error(self, manager_with_task: Manager, task: TaskModel) -> None:
        with pytest.raises(ValidationError):
            manager_with_task.move_task_by_state(id_task=task.id, state="invalid")  # type: ignore[arg-type]


class TestManagerLoggingTask:
    @pytest.mark.unit
    def test_logging_task_empty_manager_does_not_raise(self, manager: Manager) -> None:
        manager.logging_task()

    @pytest.mark.unit
    def test_logging_task_with_tasks_does_not_raise(self, manager_with_task: Manager) -> None:
        manager_with_task.logging_task()


class TestManagerFindTaskById:
    @pytest.mark.unit
    def test_find_existing_task_returns_task(self, manager_with_task: Manager, task: TaskModel) -> None:
        found: TaskModel = manager_with_task._find_task_by_id(id_task=task.id)
        assert found is task

    @pytest.mark.unit
    def test_find_nonexistent_task_raises_not_found_error(self, manager: Manager) -> None:
        ghost_task: TaskModel = TaskModel(title="Ghost", description="Ghost", expiration_date=datetime(2026, 1, 1))
        with pytest.raises(NotFoundError):
            manager._find_task_by_id(id_task=ghost_task.id)
