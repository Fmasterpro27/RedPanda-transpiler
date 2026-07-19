import argparse
from pathlib import Path

from .transpiler import transpile_file

OUTPUT_EXTENSION = ".panda"


def resolve_input_path(raw_input: str) -> Path:
    input_path = Path(raw_input)
    if input_path.exists():
        return input_path

    if input_path.drive == "" and raw_input.startswith(("/", "\\")):
        relative_path = Path(raw_input.lstrip("/\\"))
        if relative_path.exists():
            return relative_path

    return input_path


def main():
    parser = argparse.ArgumentParser(
        prog="redpanda-tr",
        description="Python → Mandarin Chinese transpiler"
    )

    parser.add_argument(
        "input",
        help="path to the Python source file to transpile (.py)"
    )

    parser.add_argument(
        "-o", "--output",
        help=f"path to write the translated output to "
             f"(defaults to <input>{OUTPUT_EXTENSION} if omitted)"
    )

    parser.add_argument(
        "--stdout",
        action="store_true",
        help="write the transpiled source to stdout instead of a file",
    )

    args = parser.parse_args()

    input_path = resolve_input_path(args.input)

    if input_path.suffix != ".py":
        parser.error(
            f"input file must have a .py extension, got '{input_path.suffix}'"
        )

    if args.stdout:
        print(transpile_file(str(input_path)))
    else:
        output_path = args.output or str(input_path.with_suffix(OUTPUT_EXTENSION))
        transpile_file(str(input_path), output_path)
        print(f"✓ Transpiled '{input_path}' → '{output_path}'")