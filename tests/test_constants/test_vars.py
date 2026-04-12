import pytest

from propel.constants.vars import States


class TestStates:
    @pytest.mark.unit
    def test_states_contains_pending(self) -> None:
        assert "pending" in States

    @pytest.mark.unit
    def test_states_contains_in_progress(self) -> None:
        assert "in_progress" in States

    @pytest.mark.unit
    def test_states_contains_complete(self) -> None:
        assert "complete" in States

    @pytest.mark.unit
    def test_states_has_exactly_three_elements(self) -> None:
        assert len(States) == 3

    @pytest.mark.unit
    def test_states_is_list(self) -> None:
        assert isinstance(States, list)

    @pytest.mark.unit
    def test_states_elements_are_strings(self) -> None:
        for state in States:
            assert isinstance(state, str)

    @pytest.mark.unit
    def test_invalid_state_not_in_states(self) -> None:
        assert "invalid" not in States

    @pytest.mark.unit
    def test_empty_string_not_in_states(self) -> None:
        assert "" not in States
