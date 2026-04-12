import logging

import pytest

from propel.configs.logger_config import setup_logger


class TestSetupLogger:
    @pytest.mark.unit
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger("test.logger")
        assert isinstance(logger, logging.Logger)

    @pytest.mark.unit
    def test_logger_has_correct_name(self) -> None:
        logger: logging.Logger = setup_logger("my.custom.logger")
        assert logger.name == "my.custom.logger"

    @pytest.mark.unit
    def test_logger_has_debug_level(self) -> None:
        logger: logging.Logger = setup_logger("test.level.logger")
        assert logger.level == logging.DEBUG

    @pytest.mark.unit
    def test_logger_has_at_least_one_handler(self) -> None:
        logger: logging.Logger = setup_logger("test.handler.logger")
        assert len(logger.handlers) >= 1

    @pytest.mark.unit
    def test_calling_twice_does_not_duplicate_handlers(self) -> None:
        name: str = "test.dedup.logger"
        setup_logger(name)
        setup_logger(name)
        logger: logging.Logger = logging.getLogger(name)
        assert len(logger.handlers) == 1

    @pytest.mark.unit
    def test_default_name_is_used_when_no_arg(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "propel"

    @pytest.mark.unit
    def test_handler_is_stream_handler(self) -> None:
        logger: logging.Logger = setup_logger("test.stream.handler")
        assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)
