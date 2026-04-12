import pytest

from propel.utils.exceptions import (
    AuthenticationError,
    BaseError,
    BusinessError,
    ConflictError,
    InternalError,
    NotFoundError,
    ValidationError,
)


class TestBaseError:
    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: BaseError = BaseError()
        assert error.message == "Internal library error."

    @pytest.mark.unit
    def test_default_code(self) -> None:
        error: BaseError = BaseError()
        assert error.code == "ERROR_INTERNAL_LIBRARY"

    @pytest.mark.unit
    def test_custom_message(self) -> None:
        error: BaseError = BaseError(message="Custom message")
        assert error.message == "Custom message"

    @pytest.mark.unit
    def test_custom_code(self) -> None:
        error: BaseError = BaseError(code="CUSTOM_CODE")
        assert error.code == "CUSTOM_CODE"

    @pytest.mark.unit
    def test_is_exception(self) -> None:
        assert issubclass(BaseError, Exception)

    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseError):
            raise BaseError()

    @pytest.mark.unit
    def test_str_is_message(self) -> None:
        error: BaseError = BaseError(message="Some error")
        assert str(error) == "Some error"


class TestValidationError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        assert issubclass(ValidationError, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: ValidationError = ValidationError()
        assert error.message == "Validation error"

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: ValidationError = ValidationError(code="MY_CODE", message="My message")
        assert error.code == "MY_CODE"
        assert error.message == "My message"

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise ValidationError()


class TestAuthenticationError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        assert issubclass(AuthenticationError, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: AuthenticationError = AuthenticationError()
        assert error.message == "Authentication error"

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise AuthenticationError()


class TestNotFoundError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        assert issubclass(NotFoundError, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: NotFoundError = NotFoundError()
        assert error.message == "Resource not found"

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise NotFoundError()


class TestConflictError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        assert issubclass(ConflictError, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: ConflictError = ConflictError()
        assert error.message == "Conflict error"

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise ConflictError()


class TestBusinessError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        assert issubclass(BusinessError, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: BusinessError = BusinessError()
        assert error.message == "Business rule violated"

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise BusinessError()


class TestInternalError:
    @pytest.mark.unit
    def test_inherits_from_base_error(self) -> None:
        assert issubclass(InternalError, BaseError)

    @pytest.mark.unit
    def test_default_message(self) -> None:
        error: InternalError = InternalError()
        assert error.message == "Internal error"

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise InternalError()
