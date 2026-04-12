import pytest

import propel.constants.codes as codes


class TestErrorCodes:
    @pytest.mark.unit
    def test_code_error_internal_library(self) -> None:
        assert codes.CODE_ERROR_INTERNAL_LIBRARY == "ERROR_INTERNAL_LIBRARY"

    @pytest.mark.unit
    def test_code_not_valid_integer(self) -> None:
        assert codes.CODE_NOT_VALID_INTEGER == "NOT_VALID_INTEGER"

    @pytest.mark.unit
    def test_code_not_valid_status_task(self) -> None:
        assert codes.CODE_NOT_VALID_STATUS_TASK == "NOT_VALID_STATUS_TASK"

    @pytest.mark.unit
    def test_code_not_valid_properties_task(self) -> None:
        assert codes.CODE_NOT_VALID_PROPERTIES_TASK == "NOT_VALID_PROPERTIES_TASK"

    @pytest.mark.unit
    def test_code_not_valid_task(self) -> None:
        assert codes.CODE_NOT_VALID_TASK == "NOT_VALID_TASK"

    @pytest.mark.unit
    def test_code_not_exists_task(self) -> None:
        assert codes.CODE_NOT_EXISTS_TASK == "NOT_EXISTS_TASK"

    @pytest.mark.unit
    def test_code_already_exists_task(self) -> None:
        assert codes.CODE_ALREADY_EXISTS_TASK == "ALREADY_EXISTS_TASK"

    @pytest.mark.unit
    def test_code_not_found_task(self) -> None:
        assert codes.CODE_NOT_FOUND_TASK == "NOT_FOUND_TASK"

    @pytest.mark.unit
    def test_all_codes_are_strings(self) -> None:
        all_codes: list[str] = [
            codes.CODE_ERROR_INTERNAL_LIBRARY,
            codes.CODE_NOT_VALID_INTEGER,
            codes.CODE_NOT_VALID_STATUS_TASK,
            codes.CODE_NOT_VALID_PROPERTIES_TASK,
            codes.CODE_NOT_VALID_TASK,
            codes.CODE_NOT_EXISTS_TASK,
            codes.CODE_ALREADY_EXISTS_TASK,
            codes.CODE_NOT_FOUND_TASK,
        ]
        for code in all_codes:
            assert isinstance(code, str)

    @pytest.mark.unit
    def test_all_codes_are_unique(self) -> None:
        all_codes: list[str] = [
            codes.CODE_ERROR_INTERNAL_LIBRARY,
            codes.CODE_NOT_VALID_INTEGER,
            codes.CODE_NOT_VALID_STATUS_TASK,
            codes.CODE_NOT_VALID_PROPERTIES_TASK,
            codes.CODE_NOT_VALID_TASK,
            codes.CODE_NOT_EXISTS_TASK,
            codes.CODE_ALREADY_EXISTS_TASK,
            codes.CODE_NOT_FOUND_TASK,
        ]
        assert len(all_codes) == len(set(all_codes))
