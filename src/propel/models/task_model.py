from datetime import datetime
from uuid import uuid4

from propel.configs.logger_config import setup_logger
from propel.constants.codes import CODE_NOT_VALID_PROPERTIES_TASK, CODE_NOT_VALID_STATUS_TASK
from propel.constants.messages import MESSAGE_NOT_VALID_PROPERTIES_TASK, MESSAGE_NOT_VALID_STATUS_TASK
from propel.constants.types import StateType
from propel.constants.vars import States
from propel.utils.exceptions import ValidationError

logger = setup_logger("propel - task_model.py")


class TaskModel:
    def __init__(
        self,
        title: str,
        description: str,
        expiration_date: datetime,
        state: StateType = "pending",
    ) -> None:
        self.__id = uuid4()
        self._title = title
        self._description = description
        self._expiration_date = expiration_date
        self.__state = state

    @property
    def id(self) -> str:
        return str(self.__id)

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def expiration_date(self) -> datetime:
        return self._expiration_date

    @property
    def state(self) -> str:
        return self.__state

    def change_state(self, state: StateType) -> None:
        if state not in States:
            raise ValidationError(code=CODE_NOT_VALID_STATUS_TASK, message=MESSAGE_NOT_VALID_STATUS_TASK)

        previous_state = self.state
        self.__state = state
        logger.info(f"{self._title} task with {previous_state} status was changed to {state}")

    def edit(self, title: str = "", description: str = "", expiration_date: datetime | None = None) -> None:
        if not title and not description and not expiration_date:
            raise ValidationError(code=CODE_NOT_VALID_PROPERTIES_TASK, message=MESSAGE_NOT_VALID_PROPERTIES_TASK)

        dict = {
            "_title": title,
            "_description": description,
            "_expiration_date": expiration_date,
        }

        for key, value in dict.items():
            if value:
                setattr(self, key, value)

    def __str__(self) -> str:
        return f"TaskModel: {self.id}\nTitle: {self._title}\nDescription: {self._description}\nExpiration Date: {self._expiration_date}\nState: {self.state}"
