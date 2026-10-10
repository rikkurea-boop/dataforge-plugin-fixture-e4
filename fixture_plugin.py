def handle(operation: str, payload: dict[str, object]) -> dict[str, object]:
    if operation != "process":
        raise ValueError("unsupported operation")
    text = payload.get("text")
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    return {"text": text.upper()}
