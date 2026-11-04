"""Pure, dependency-free editorial checks for synthetic examples.

Not a news fact-checker, network security filter or production policy engine.
"""
from dataclasses import dataclass
from urllib.parse import urlsplit


@dataclass(frozen=True)
class ValidationIssue:
    field: str
    message: str


def validate_summary(title: str, summary: str, *, max_words: int = 90) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if not isinstance(title, str) or not title.strip():
        issues.append(ValidationIssue("title", "A non-empty title is required."))
    if not isinstance(summary, str) or not summary.strip():
        issues.append(ValidationIssue("summary", "A non-empty summary is required."))
    elif len(summary.split()) > max_words:
        issues.append(ValidationIssue("summary", f"Summary exceeds {max_words} words."))
    return issues


def validate_source_url(url: str) -> list[ValidationIssue]:
    """Check basic syntax only; never use this as an SSRF defense."""
    if not isinstance(url, str) or not url or any(c.isspace() for c in url):
        return [ValidationIssue("source_url", "Expected an absolute HTTP(S) URL.")]
    try:
        parts = urlsplit(url)
        valid = parts.scheme in {"http", "https"} and bool(parts.hostname) and not parts.username and not parts.password
    except ValueError:
        valid = False
    return [] if valid else [ValidationIssue("source_url", "Expected an absolute HTTP(S) URL without embedded credentials.")]
