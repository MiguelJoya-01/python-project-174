# Difference Calculator

[![Python CI](https://github.com/MiguelJoya-01/python-project-174/actions/workflows/pyci.yml/badge.svg)](https://github.com/MiguelJoya-01/python-project-174/actions/workflows/pyci.yml)

A command-line utility and Python library for comparing configuration files in JSON and YAML formats.

## Requirements

- Python 3.12 or higher
- uv

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/MiguelJoya-01/python-project-174.git
cd python-project-174
```

Install the project dependencies:

```bash
uv sync
```

## Usage

Compare two JSON files:

```bash
uv run gendiff file1.json file2.json
```

Compare two YAML files:

```bash
uv run gendiff file1.yml file2.yml
```

The utility also supports files with the `.yaml` extension.

### Output format

The default output format is `stylish`. You can specify it explicitly using `--format`:

```bash
uv run gendiff --format stylish file1.json file2.json
```

## Features

- Supports JSON, YAML, and YML configuration files.
- Recursively compares nested dictionaries.
- Detects added, removed, changed, and unchanged properties.
- Displays differences using the `stylish` format.
- Uses `stylish` as the default output format.
- Supports the `--format` command-line option.
- Separates difference calculation from output formatting.
- Provides a reusable Python function.

## Example

Given two configuration files with nested structures, `gendiff` recursively compares their contents.

**file1.json**

```json
{
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "follow": false
  },
  "group1": {
    "baz": "bas",
    "foo": "bar"
  }
}
```

**file2.json**

```json
{
  "common": {
    "setting1": "Value 1",
    "setting2": 300,
    "follow": true
  },
  "group1": {
    "baz": "bars",
    "foo": "bar"
  }
}
```

Run the comparison:

```bash
uv run gendiff file1.json file2.json
```

Output:

```text
{
    common: {
      - follow: false
      + follow: true
        setting1: Value 1
      - setting2: 200
      + setting2: 300
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
    }
}
```

The output uses the following markers:

- `+` indicates an added property or a new value.
- `-` indicates a removed property or an old value.
- No marker indicates an unchanged property.
- Nested objects are displayed recursively.

## Python Library

You can use `generate_diff()` directly from Python:

```python
from gendiff import generate_diff

diff = generate_diff("file1.json", "file2.json")
print(diff)
```

The output format can also be specified explicitly:

```python
from gendiff import generate_diff

diff = generate_diff(
    "file1.json",
    "file2.json",
    "stylish",
)
print(diff)
```

## Tests

Run the test suite:

```bash
uv run pytest
```

Run tests with coverage:

```bash
make test-coverage
```

Run the linter:

```bash
make lint
```

## Demo

### JSON comparison

[![JSON comparison demo](https://asciinema.org/a/NbjN7VAxX8bFp8RV.svg)](https://asciinema.org/a/NbjN7VAxX8bFp8RV)

### YAML comparison

[![YAML comparison demo](https://asciinema.org/a/8kDJNVZ4vCrR9NoD.svg)](https://asciinema.org/a/8kDJNVZ4vCrR9NoD)

### Recursive comparison and stylish format

[![Recursive comparison demo](https://asciinema.org/a/sSck2ZwHaGLt0rR9.svg)](https://asciinema.org/a/sSck2ZwHaGLt0rR9)
