def str_to_bool(string: str) -> bool:
    """Converts string to bool.

    Args:
        string (str): ("Yes", "No", "True", "False", "1", "0")

    Returns:
        bool
    """
    if isinstance(string, bool):
        return string

    if string is None:
        return False

    if string.lower() in ("yes", "true", "t", "y", "1"):
        return True

    elif string.lower() in ("no", "false", "f", "n", "0"):
        return False

    return False
