import os

from . import constants


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


type_deserializers = {
    bool: str2bool,
    int: int
}


def environ_or_default(environ_name=None, default=None, type_override=None):
    """Look up value from environment variable and fallback to default.  All variable references will be prefixed."""

    # Short circuit if no environ_name is set
    if not environ_name:
        return default

    result = os.environ.get(constants.ENVIRON_PREFIX + '_' + environ_name, default=default)

    if not result or result == default:
        # Handle case where env var exists but has no value
        result = default
    elif type_override and type_deserializers.get(type_override):
        result = type_deserializers.get(type_override)(result)

    return result
