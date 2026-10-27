# Gendiff

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

### Output formats

The default output format is `stylish`. You can specify it explicitly using `--format`:

```bash
uv run gendiff --format stylish file1.json file2.json
```

Gendiff also supports the `plain` output format:

```bash
uv run gendiff --format plain file1.json file2.json
```

#### Stylish format

The `stylish` format displays differences in a structured, tree-like format. Added and removed properties are marked with `+` and `-`, respectively.

Example:

```text
{
  common: {
    + follow: false
      setting1: Value 1
    - setting2: 200
    + setting2: 300
  }
}
```

#### Plain format

The `plain` format describes changes using sentences and full property paths.

Example:

```text
Property 'common.follow' was added with value: false
Property 'common.setting2' was updated. From 200 to 300
```

The plain formatter follows these rules:

- Added properties include their new values.
- Removed properties are reported without a value.
- Updated properties display their previous and new values.
- Unchanged properties are omitted.
- Nested properties are represented by their full paths, separated by dots.
- Complex values, such as objects and lists, are represented as `[complex value]`.
- Strings are enclosed in single quotes.
- Boolean and null values are displayed as `true`, `false`, and `null`.

## Features

- Compare JSON and YAML configuration files.
- Detect added, removed, updated, and unchanged properties.
- Compare nested objects recursively.
- Display differences in `stylish` or `plain` format.
- Use Gendiff from the command line or as a Python library.

## Python library usage

Gendiff can also be used from Python code:

```python
from gendiff import generate_diff

diff = generate_diff("file1.json", "file2.json")
print(diff)
```

To select a specific output format, pass it as the third argument:

```python
from gendiff import generate_diff

diff = generate_diff("file1.json", "file2.json", "plain")
print(diff)
```

## Development

Run the test suite:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=gendiff --cov-report=term-missing
```

Run the linter:

```bash
make lint
```

## Demonstrations

### JSON files

[![JSON demonstration](https://asciinema.org/a/NbjN7VAxX8bFp8RV.svg)](https://asciinema.org/a/NbjN7VAxX8bFp8RV)

### YAML files

[![YAML demonstration](https://asciinema.org/a/8kDJNVZ4vCrR9NoD.svg)](https://asciinema.org/a/8kDJNVZ4vCrR9NoD)

### Recursive comparison and stylish output

[![Recursive comparison demonstration](https://asciinema.org/a/sSck2ZwHaGLt0rR9.svg)](https://asciinema.org/a/sSck2ZwHaGLt0rR9)

### Plain output

[![Plain output demonstration](https://asciinema.org/a/Fm1cUu0BW4D8Y9hp.svg)](https://asciinema.org/a/Fm1cUu0BW4D8Y9hp)

## License

This project was developed as part of a programming learning project.
