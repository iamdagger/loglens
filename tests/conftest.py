"""Shared test fixtures."""
import pytest


@pytest.fixture
def sample_lines():
    """Standard log lines covering all severity levels."""
    return [
        "2026-09-20T10:00:00Z INFO service started",
        "2026-09-20T10:00:01Z WARN disk usage 89%",
        "2026-09-20T10:00:02Z ERROR connection refused",
        "2026-09-20T10:00:03Z DEBUG cache hit ratio=0.97",
    ]
