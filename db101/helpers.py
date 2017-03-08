import re

# https://stackoverflow.com/a/12867228
_CAMELCASE_RE = re.compile(r"((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))")


def camelcase_to_snakecase(camel):
    return _CAMELCASE_RE.sub(r"_\1", camel).lower()
