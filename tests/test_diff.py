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
