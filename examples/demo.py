"""Demo entry point for the propel library.

Run with:
    python -m examples.demo
or (if installed via `pip install -e .`):
    propel-demo
"""

from datetime import datetime

from propel import Manager, TaskModel
from propel.configs.logger_config import setup_logger

logger = setup_logger("propel - examples/demo.py")


def main() -> None:
    task_manager = Manager()

    task_1 = TaskModel(
        title="Diseñar base de datos",
        description="Crear el esquema inicial de la base de datos relacional.",
        expiration_date=datetime(year=2026, month=6, day=1),
    )
    task_2 = TaskModel(
        title="Implementar autenticación",
        description="Agregar login y registro con JWT.",
        expiration_date=datetime(year=2026, month=6, day=15),
    )
    task_3 = TaskModel(
        title="Escribir tests de integración",
        description="Cubrir los endpoints principales con tests de integración.",
        expiration_date=datetime(year=2026, month=7, day=1),
    )

    task_manager.add_task(task=task_1)
    task_manager.add_task(task=task_2)
    task_manager.add_task(task=task_3)

    task_manager.move_task_by_state(id_task=task_1.id, state="in_progress")
    task_manager.move_task_by_state(id_task=task_2.id, state="in_progress")

    task_manager.edit_task(
        id_task=task_1.id,
        description="Crear el esquema inicial con migraciones usando Alembic.",
    )

    task_manager.move_task_by_state(id_task=task_1.id, state="complete")

    task_manager.logging_task()


if __name__ == "__main__":
    main()
