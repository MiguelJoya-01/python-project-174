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
