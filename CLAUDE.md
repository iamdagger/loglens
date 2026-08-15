# loglens

## Setup

```bash
pip install -e ".[test]"
```

## Testing

```bash
pytest
```

## About

A zero-dependency structured-log parser. The public API is a single function:
`loglens.parse(line)` returns a dict or None.
