from loglens import parse


def test_info_line():
    r = parse("2026-09-20T10:00:00Z INFO service started")
    assert r["level"] == "INFO"
    assert r["msg"] == "service started"


def test_error_line():
    r = parse("2026-09-20T10:00:00Z ERROR connection refused")
    assert r["level"] == "ERROR"
    assert r["ts"] == "2026-09-20T10:00:00Z"


def test_debug_with_extra_fields():
    r = parse("2026-09-20T10:00:00Z DEBUG cache hit ratio=0.97")
    assert r["level"] == "DEBUG"
    assert "ratio=0.97" in r["msg"]


def test_warn_level():
    r = parse("2026-09-20T10:00:00Z WARN disk usage above 90%")
    assert r["level"] == "WARN"


def test_critical_level():
    r = parse("2026-09-20T10:00:00Z CRITICAL out of memory")
    assert r["level"] == "CRITICAL"


def test_preserves_full_message():
    r = parse("2026-09-20T10:00:00Z INFO user login id=42 ip=10.0.0.1")
    assert r["msg"] == "user login id=42 ip=10.0.0.1"


def test_rejects_garbage():
    assert parse("not a valid line") is None


def test_rejects_empty():
    assert parse("") is None


def test_rejects_whitespace():
    assert parse("   ") is None


def test_strips_whitespace():
    r = parse("  2026-09-20T10:00:00Z INFO padded  ")
    assert r is not None
    assert r["level"] == "INFO"
