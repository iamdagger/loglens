"""loglens - tiny structured-log line parser."""
import re

__version__ = "1.2.0"

_LINE = re.compile(r"^(?P<ts>\S+)\s+(?P<level>[A-Z]+)\s+(?P<msg>.*)$")


def parse(line):
    """Parse one structured log line into a dict, or None if it doesn't match."""
    m = _LINE.match(line.strip())
    if not m:
        return None
    return {"ts": m.group("ts"), "level": m.group("level"), "msg": m.group("msg")}
