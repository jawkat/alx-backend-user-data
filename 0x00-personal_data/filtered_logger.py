#!/usr/bin/env python3
""" commants task 0 """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Args:
        fields (List[str]): List of field names to obfuscate.
        redaction (str): The string to replace the field values with.
        message (str): The log line containing the fields and values.
        separator (str): The character separating the fields in the log line.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    return re.sub(f'({"|".join(fields)})=[^{separator}]+',
                  lambda m: f"{m.group(1)}={redaction}", message)
