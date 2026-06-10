# loglens

[![CI](https://github.com/iamdagger/loglens/actions/workflows/ci.yml/badge.svg)](https://github.com/iamdagger/loglens/actions/workflows/ci.yml)
![python](https://img.shields.io/badge/python-3.8%2B-blue)
![license](https://img.shields.io/badge/license-MIT-green)
[![PyPI](https://img.shields.io/badge/pypi-v1.2.0-blue)](https://pypi.org/project/loglens/)

Tiny structured-log parser for Python. One function, zero dependencies, works
on every line format you actually see in the wild.

Feed it a raw log line, get back a clean dict with `ts`, `level`, and `msg`
separated and ready for filtering, indexing, or piping into whatever comes
next.

## Why

Every log pipeline starts the same way: split the timestamp, pull the level,
keep the message. loglens does exactly that in a single `parse()` call so you
can skip the regex boilerplate and get to the part that matters.

If your logs are already JSON, use `json.loads`. If they are human-readable
structured lines (timestamps, levels, messages), loglens is the faster path.

## Install

```bash
pip install loglens
```

Or from source:

```bash
git clone https://github.com/iamdagger/loglens.git
cd loglens
pip install -e .
```

## Quick start

```python
from loglens import parse

line = "2026-09-20T10:00:00Z INFO service started"
result = parse(line)
# {'ts': '2026-09-20T10:00:00Z', 'level': 'INFO', 'msg': 'service started'}
```

## Supported formats

loglens handles the most common structured-log patterns out of the box:

| Format | Example |
|--------|---------|
| ISO 8601 | `2026-09-20T10:00:00Z INFO service started` |
| Datetime | `2026-09-20 10:00:00 ERROR connection refused` |
| Epoch prefix | `1695206400 WARN disk usage above 90%` |
| Syslog-ish | `Sep 20 10:00:00 CRITICAL out of memory` |

All formats are matched by the same `parse()` function. If a line does not
match any known pattern, `parse()` returns `None` instead of raising.

## API

### `parse(line: str) -> dict | None`

Parse one structured log line into a dict with keys `ts`, `level`, and `msg`.
Returns `None` if the line does not match a known format.

```python
>>> parse("2026-09-20T10:00:00Z DEBUG cache hit ratio=0.97")
{'ts': '2026-09-20T10:00:00Z', 'level': 'DEBUG', 'msg': 'cache hit ratio=0.97'}

>>> parse("not a log line")
None
```

### `__version__`

```python
>>> import loglens
>>> loglens.__version__
'1.2.0'
```

## Development

```bash
git clone https://github.com/iamdagger/loglens.git
cd loglens
pip install -e .
pip install pytest
pytest
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Contributing

Pull requests welcome. Please include tests for new formats and keep the
zero-dependency constraint. Run `pytest` before submitting.

## License

MIT. See [LICENSE](LICENSE) for the full text.
