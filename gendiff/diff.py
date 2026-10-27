from gendiff.parsers import parse_file


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def generate_diff(first_file, second_file):
    data1 = parse_file(first_file)
    data2 = parse_file(second_file)

    lines = ["{"]

    for key in sorted(data1.keys() | data2.keys()):
        if key not in data2:
            lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1:
            lines.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {format_value(data1[key])}")
        else:
            lines.append(f"  - {key}: {format_value(data1[key])}")
            lines.append(f"  + {key}: {format_value(data2[key])}")

    lines.append("}")
    return "\n".join(lines)
