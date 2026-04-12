from typing import get_args

import pytest

from propel.constants.types import StateType


class TestStateType:
    @pytest.mark.unit
    def test_state_type_includes_pending(self) -> None:
        assert "pending" in get_args(StateType)

    @pytest.mark.unit
    def test_state_type_includes_in_progress(self) -> None:
        assert "in_progress" in get_args(StateType)

    @pytest.mark.unit
    def test_state_type_includes_complete(self) -> None:
        assert "complete" in get_args(StateType)

    @pytest.mark.unit
    def test_state_type_has_exactly_three_values(self) -> None:
        assert len(get_args(StateType)) == 3

    @pytest.mark.unit
    def test_state_type_values_are_strings(self) -> None:
        for value in get_args(StateType):
            assert isinstance(value, str)
