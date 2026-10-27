def format_value(value, depth):
    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return "null"

    if isinstance(value, dict):
        lines = ["{"]
        for key in sorted(value):
            formatted = format_value(value[key], depth + 1)
            lines.append(f"{' ' * (depth * 4)}{key}: {formatted}")
        lines.append(f"{' ' * ((depth - 1) * 4)}}}")
        return "\n".join(lines)

    return str(value)


def stylish(diff, depth=1):
    lines = ["{"]

    for node in diff:
        key = node["key"]
        node_type = node["type"]

        if node_type == "nested":
            value = stylish(node["children"], depth + 1)
            lines.append(f"{' ' * (depth * 4)}{key}: {value}")

        elif node_type == "unchanged":
            value = format_value(node["value"], depth + 1)
            lines.append(f"{' ' * (depth * 4)}{key}: {value}")

        elif node_type == "added":
            value = format_value(node["value"], depth + 1)
            lines.append(
                f"{' ' * (depth * 4 - 2)}+ {key}: {value}"
            )

        elif node_type == "removed":
            value = format_value(node["value"], depth + 1)
            lines.append(
                f"{' ' * (depth * 4 - 2)}- {key}: {value}"
            )

        elif node_type == "changed":
            old_value = format_value(node["old_value"], depth + 1)
            new_value = format_value(node["new_value"], depth + 1)

            lines.append(
                f"{' ' * (depth * 4 - 2)}- {key}: {old_value}"
            )
            lines.append(
                f"{' ' * (depth * 4 - 2)}+ {key}: {new_value}"
            )

    lines.append(f"{' ' * ((depth - 1) * 4)}}}")
    return "\n".join(lines)
