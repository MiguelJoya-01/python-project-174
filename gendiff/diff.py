from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parsers import parse_file
from gendiff.tree import build_diff


def generate_diff(first_file, second_file, format_name="stylish"):
    data1 = parse_file(first_file)
    data2 = parse_file(second_file)

    diff = build_diff(data1, data2)

    if format_name == "stylish":
        return stylish(diff)

    if format_name == "plain":
        return plain(diff)

    raise ValueError(f"Unsupported format: {format_name}")
