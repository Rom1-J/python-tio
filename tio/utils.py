from zlib import compress
from typing import List

from tio.contants import NULL, PAYLOAD
from tio.exceptions import WrappingNotFound


def shortcut(lang: str) -> str:
    replacements = {
        "py": "python3",
        "python": "python3",
        "js": "javascript",
        "sh": "bash",
        "asm": "assembly",
        "c#": "cs",
        "csharp": "cs",
        "c++": "cpp",
    }

    if lang in replacements:
        return replacements[lang]

    return lang


def wrapper(lang: str, code: str):
    # fmt: off
    wrapping = {
        "c": (
            "#include <stdio.h>\n"
            "int main() {"
            "[content]"
            "}"
        ),
        "cpp": (
            "#include <iostream>\n"
            "int main() {"
            "[content]"
            "}"
        ),
        "cs": (
            "using System;"
            "class Program {"
            "static void Main(string[] args) {"
            "[content]"
            "}"
            "}"
        ),
        "java": (
            "public class Main {"
            "public static void main(String[] args) {"
            "[content]"
            "}"
            "}"
        ),
        "rust": (
            "fn main() {"
            "[content]"
            "}"
        ),
    }
    # fmt: on

    if lang not in wrapping:
        raise WrappingNotFound

    return wrapping[lang].replace("[content]", code)


def tio_bytes(row: tuple) -> bytes:
    key, value = row

    if not value:
        return b""

    if isinstance(value, list):
        content = ["V" + key, str(len(value))] + value
        return f"{NULL.join(content)}{NULL}".encode()

    return f"F{key}{NULL}{len(value.encode())}{NULL}{value}{NULL}".encode()


def prepare_payload(
    lang: str, code: str, inputs: str = "", wrapped: bool = False, **kwargs
) -> bytes:
    compiler_flags: List[str] = kwargs.get("compiler_flags", [])
    cli_options: List[str] = kwargs.get("cli_options", [])
    args: List[str] = kwargs.get("args", [])

    if wrapped:
        code = wrapper(lang, code)

    payload = PAYLOAD

    payload["lang"] = [lang]
    payload[".code.tio"] = code
    payload[".input.tio"] = inputs
    payload["TIO_CFLAGS"] = compiler_flags
    payload["TIO_OPTIONS"] = cli_options
    payload["args"] = args

    return compress(
        b"".join(map(tio_bytes, zip(payload.keys(), payload.values()))) + b"R",
        9,
    )[2:-4]


def clean_result(text: str) -> str:
    text = text.replace(text[:16], "")

    lines = text.split("\n")

    good_lines = lines[:-5]
    good_lines.append(lines[-1])

    return "\n".join(good_lines)
