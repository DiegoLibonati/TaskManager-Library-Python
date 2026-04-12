import pytest

import propel.constants.messages as messages


class TestMessages:
    @pytest.mark.unit
    def test_message_error_internal_library(self) -> None:
        assert messages.MESSAGE_ERROR_INTERNAL_LIBRARY == "Internal library error."

    @pytest.mark.unit
    def test_message_not_valid_integer(self) -> None:
        assert messages.MESSAGE_NOT_VALID_INTEGER == "The value entered is not a valid integer."

    @pytest.mark.unit
    def test_message_not_valid_status_task(self) -> None:
        assert messages.MESSAGE_NOT_VALID_STATUS_TASK == "The status entered is not a valid."

    @pytest.mark.unit
    def test_message_not_valid_properties_task(self) -> None:
        assert messages.MESSAGE_NOT_VALID_PROPERTIES_TASK == "The properties entered are not valid."

    @pytest.mark.unit
    def test_message_not_valid_task(self) -> None:
        assert messages.MESSAGE_NOT_VALID_TASK == "The task entered is not valid."

    @pytest.mark.unit
    def test_message_not_exists_task(self) -> None:
        assert messages.MESSAGE_NOT_EXISTS_TASK == "The task not exists."

    @pytest.mark.unit
    def test_message_already_exists_task(self) -> None:
        assert messages.MESSAGE_ALREADY_EXISTS_TASK == "The task already exists."

    @pytest.mark.unit
    def test_message_not_found_task(self) -> None:
        assert messages.MESSAGE_NOT_FOUND_TASK == "Not found task."

    @pytest.mark.unit
    def test_all_messages_are_strings(self) -> None:
        all_messages: list[str] = [
            messages.MESSAGE_ERROR_INTERNAL_LIBRARY,
            messages.MESSAGE_NOT_VALID_INTEGER,
            messages.MESSAGE_NOT_VALID_STATUS_TASK,
            messages.MESSAGE_NOT_VALID_PROPERTIES_TASK,
            messages.MESSAGE_NOT_VALID_TASK,
            messages.MESSAGE_NOT_EXISTS_TASK,
            messages.MESSAGE_ALREADY_EXISTS_TASK,
            messages.MESSAGE_NOT_FOUND_TASK,
        ]
        for message in all_messages:
            assert isinstance(message, str)

    @pytest.mark.unit
    def test_all_messages_are_unique(self) -> None:
        all_messages: list[str] = [
            messages.MESSAGE_ERROR_INTERNAL_LIBRARY,
            messages.MESSAGE_NOT_VALID_INTEGER,
            messages.MESSAGE_NOT_VALID_STATUS_TASK,
            messages.MESSAGE_NOT_VALID_PROPERTIES_TASK,
            messages.MESSAGE_NOT_VALID_TASK,
            messages.MESSAGE_NOT_EXISTS_TASK,
            messages.MESSAGE_ALREADY_EXISTS_TASK,
            messages.MESSAGE_NOT_FOUND_TASK,
        ]
        assert len(all_messages) == len(set(all_messages))
