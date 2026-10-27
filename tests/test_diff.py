import sys

from gendiff import generate_diff
from gendiff.scripts.gendiff import main


def test_generate_diff():
    result = generate_diff("file1.json", "file2.json")

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert result == expected


def test_main(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["gendiff", "file1.json", "file2.json"],
    )

    main()

    captured = capsys.readouterr()
    assert "host: hexlet.io" in captured.out
    assert captured.out.startswith("{")


def test_generate_diff_yaml():
    result = generate_diff("file1.yml", "file2.yml")

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert result == expected


def test_generate_diff_yaml_extension():
    result = generate_diff("file1.yaml", "file2.yaml")

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert result == expected


def test_generate_diff_nested(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        '{"common": {"setting1": "Value 1", "setting2": 200}}',
        encoding="utf-8",
    )
    file2.write_text(
        '{"common": {"setting1": "Value 1", "setting2": 300, "follow": false}}',
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2))

    expected = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      + setting2: 300
    }
}"""

    assert result == expected


def test_generate_diff_nested_yaml(tmp_path):
    file1 = tmp_path / "file1.yaml"
    file2 = tmp_path / "file2.yaml"

    file1.write_text(
        "common:\n  setting1: Value 1\n  setting2: 200\n",
        encoding="utf-8",
    )
    file2.write_text(
        "common:\n  setting1: Value 1\n  setting2: 300\n  follow: false\n",
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2))

    expected = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      + setting2: 300
    }
}"""

    assert result == expected

def test_generate_diff_nested_to_scalar(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        '{"group1": {"nest": {"key": "value"}}}',
        encoding="utf-8",
    )
    file2.write_text(
        '{"group1": {"nest": "str"}}',
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2))

    expected = """{
    group1: {
      - nest: {
            key: value
        }
      + nest: str
    }
}"""

    assert result == expected

def test_generate_diff_plain(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        '{"common": {"setting1": "Value 1", "setting2": 200}}',
        encoding="utf-8",
    )
    file2.write_text(
        '{"common": {"setting1": "Value 1", "setting2": 300, "follow": false}}',
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2), "plain")

    expected = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was updated. From 200 to 300"
    )

    assert result == expected


def test_generate_diff_plain_nested(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        '{"group1": {"nest": {"key": "value"}}}',
        encoding="utf-8",
    )
    file2.write_text(
        '{"group1": {"nest": "str"}}',
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2), "plain")

    expected = (
        "Property 'group1.nest' was updated. "
        "From [complex value] to 'str'"
    )

    assert result == expected


def test_generate_diff_plain_complex_value(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        '{"items": 1}',
        encoding="utf-8",
    )
    file2.write_text(
        '{"items": {"nested": true}}',
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2), "plain")

    expected = (
        "Property 'items' was updated. "
        "From 1 to [complex value]"
    )

    assert result == expected

def test_generate_diff_plain_removed(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        '{"common": {"setting2": 200}}',
        encoding="utf-8",
    )
    file2.write_text(
        '{"common": {}}',
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2), "plain")

    assert result == "Property 'common.setting2' was removed"


def test_generate_diff_plain_string_and_null(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        '{"name": "Miguel", "active": true}',
        encoding="utf-8",
    )
    file2.write_text(
        '{"name": "", "active": null}',
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2), "plain")

    expected = (
        "Property 'active' was updated. From true to null\n"
        "Property 'name' was updated. From 'Miguel' to ''"
    )

    assert result == expected


def test_generate_diff_unsupported_format(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text('{"key": 1}', encoding="utf-8")
    file2.write_text('{"key": 2}', encoding="utf-8")

    try:
        generate_diff(str(file1), str(file2), "unsupported")
    except ValueError as error:
        assert str(error) == "Unsupported format: unsupported"
    else:
        raise AssertionError("Expected ValueError")

def test_generate_diff_json(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        '{"setting1": "Value 1", "setting2": 200}',
        encoding="utf-8",
    )
    file2.write_text(
        '{"setting1": "Value 1", "setting2": 300, "follow": false}',
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2), "json")

    import json

    parsed = json.loads(result)

    assert isinstance(parsed, list)
    assert parsed == [
        {"key": "follow", "type": "added", "value": False},
        {
            "key": "setting1",
            "type": "unchanged",
            "value": "Value 1",
        },
        {
            "key": "setting2",
            "type": "changed",
            "old_value": 200,
            "new_value": 300,
        },
    ]


def test_generate_diff_json_nested(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"

    file1.write_text(
        '{"common": {"setting": 1}}',
        encoding="utf-8",
    )
    file2.write_text(
        '{"common": {"setting": 2}}',
        encoding="utf-8",
    )

    result = generate_diff(str(file1), str(file2), "json")

    import json

    parsed = json.loads(result)

    assert parsed == [
        {
            "key": "common",
            "type": "nested",
            "children": [
                {
                    "key": "setting",
                    "type": "changed",
                    "old_value": 1,
                    "new_value": 2,
                }
            ],
        }
    ]
