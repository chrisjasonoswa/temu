import json
import hashlib
from dataclasses import dataclass, fields, is_dataclass

def serialize_value(value):
    """Serializes a value to a JSON-compatible format."""
    if isinstance(value, (dict, list)):
        return json.dumps(value, separators=(',', ':'), ensure_ascii=False)
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, object):
        # Handle dataclasses or any class instance
        if hasattr(value, '__dict__'):
            # If it's a dataclass or custom class, serialize its attributes
            if is_dataclass(value):
                return {field.name: serialize_value(getattr(value, field.name)) for field in fields(value)}
            return {k: serialize_value(v) for k, v in value.__dict__.items()}
    return str(value)

def add_sign(params: dict, app_secret: str) -> dict:
    """
    Adds a 'sign' parameter to the payload using Temu's signature rules.
    Handles list of objects by serializing to JSON strings with double quotes.
    Handles Boolean values as lowercase 'true' or 'false'.
    Handles custom classes and dataclasses.
    """
    # Convert values (especially dicts/lists and custom classes/dataclasses) to JSON strings if needed
    serialized_params = {
        k: serialize_value(v) for k, v in params.items()
    }

    # Sort parameters alphabetically by key
    sorted_items = sorted(serialized_params.items())

    # Concatenate key + value strings
    param_str = ''.join([f"{k}{v}" for k, v in sorted_items])
    
    # Build the final signature string and calculate MD5
    sign_string = app_secret + param_str + app_secret
    print("Signature String:", sign_string)  # Debugging line to see the signature string
    sign = hashlib.md5(sign_string.encode('utf-8')).hexdigest().upper()

    return {**params, "sign": sign}
