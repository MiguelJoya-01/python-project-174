def format_value(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"

    if isinstance(value, str):
        return f"'{value}'"

    if value is True:
        return "true"

    if value is False:
        return "false"

    if value is None:
        return "null"

    return str(value)


def plain(diff, path=""):
    lines = []

    for node in diff:
        key = node["key"]
        node_type = node["type"]
        current_path = f"{path}.{key}" if path else key

        if node_type == "nested":
            lines.append(plain(node["children"], current_path))

        elif node_type == "added":
            value = format_value(node["value"])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )

        elif node_type == "removed":
            lines.append(f"Property '{current_path}' was removed")

        elif node_type == "changed":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return "\n".join(line for line in lines if line)
