from urllib.parse import urlparse


ALLOWED_DOMAINS = {
    "google.com",
    "www.google.com",
    "example.com",
    "www.example.com",
    "weather.com",
    "www.weather.com",
    "wikipedia.org",
    "www.wikipedia.org",
}

RISKY_KEYWORDS = {
    "delete",
    "remove",
    "submit",
    "purchase",
    "buy",
    "pay",
    "transfer",
    "send",
    "confirm",
    "share",
    "upload",
    "logout",
    "sign out",
}


def normalize_domain(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme and parsed.netloc:
        return parsed.netloc.lower()
    return url.lower().strip()


def is_allowed_url(url: str) -> bool:
    domain = normalize_domain(url)
    return domain in ALLOWED_DOMAINS


def text_looks_risky(text: str) -> bool:
    t = text.lower()
    return any(word in t for word in RISKY_KEYWORDS)


def confirm_risky_action(reason: str) -> bool:
    answer = input(f"[CONFIRM] {reason} Proceed? (yes/no): ").strip().lower()
    return answer in {"y", "yes"}