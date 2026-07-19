import io
import tokenize
from pathlib import Path

from .loader import KEYWORDS, BUILTINS, CONSTANTS


def build_translation_table(*tables: dict) -> dict:
    """Merge translation tables, refusing to silently overwrite a key."""
    merged: dict = {}
    for table in tables:
        overlap = merged.keys() & table.keys()
        if overlap:
            raise ValueError(f"Duplicate translation keys found: {overlap}")
        merged.update(table)
    return merged


TRANSLATIONS = build_translation_table(KEYWORDS, BUILTINS, CONSTANTS)


def transpile_source(source: str) -> str:
    """
    Translate Python source into Mandarin-keyword Python.

    Only NAME tokens (keywords, builtins, and known constants) are
    translated. Strings, comments, numbers, and operators are left
    untouched, so this is safe for things like `print("print")`.

    Note: this is a cosmetic transpiler. The output is not valid
    Python and cannot be run directly by CPython. A reverse-translation
    step (or a custom interpreter) would be needed to execute it.
    """
    tokens = []
    readline = io.StringIO(source).readline

    for tok in tokenize.generate_tokens(readline):
        toktype, tokval, start, end, line = tok

        if toktype == tokenize.NAME and tokval in TRANSLATIONS:
            tokval = TRANSLATIONS[tokval]

        tokens.append((toktype, tokval, start, end, line))

    return tokenize.untokenize(tokens)


def transpile_file(input_file: str, output_file: str | None = None) -> str:
    source = Path(input_file).read_text(encoding="utf-8")
    result = transpile_source(source)

    if output_file:
        Path(output_file).write_text(result, encoding="utf-8")

    return result