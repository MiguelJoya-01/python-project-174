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

Compare two YAML files using either `.yml` or `.yaml` extensions:

```bash
uv run gendiff file1.yml file2.yml
```

```bash
uv run gendiff file1.yaml file2.yaml
```

Example output:

```text
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

You can also use the library from Python:

```python
from gendiff import generate_diff

diff = generate_diff("file1.json", "file2.json")
print(diff)
```

The `generate_diff()` function also supports YAML files.

## Features

- Compares JSON and YAML configuration files.
- Supports `.yml` and `.yaml` extensions.
- Displays added, removed, changed, and unchanged keys.
- Sorts keys alphabetically.
- Provides a reusable `generate_diff()` function.

## Demo

### JSON comparison

Watch the command-line utility in action:

[![JSON demo](https://asciinema.org/a/NbjN7VAxX8bFp8RV.svg)](https://asciinema.org/a/NbjN7VAxX8bFp8RV)

### YAML comparison

Watch the command-line utility compare YAML files:

[![YAML demo](https://asciinema.org/a/8kDJNVZ4vCrR9NoD.svg)](https://asciinema.org/a/8kDJNVZ4vCrR9NoD)
