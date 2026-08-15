# Changelog

## 1.2.0 (2026-08-15)
- Improve timestamp matching for epoch-prefixed lines.
- Add CI session reporting for test matrix optimization.

## 1.1.0 (2026-07-02)
- Handle datetime-style timestamps (`2026-09-20 10:00:00`).
- Return `None` for unmatched lines instead of raising `ValueError`.

## 1.0.0 (2026-06-10)
- Initial release. Supports ISO 8601 timestamps with standard log levels.
