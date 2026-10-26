# Difference Calculator

[![Python CI](https://github.com/MiguelJoya-01/python-project-174/actions/workflows/pyci.yml/badge.svg)](https://github.com/MiguelJoya-01/python-project-174/actions/workflows/pyci.yml)

A command-line utility and Python library for comparing two configuration files.

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

## Features

- Compares JSON configuration files.
- Displays added, removed, changed, and unchanged keys.
- Sorts keys alphabetically.
- Provides a reusable `generate_diff()` function.

## Demo

Watch the command-line utility in action:

[![asciicast](https://asciinema.org/a/NbjN7VAxX8bFp8RV.svg)](https://asciinema.org/a/NbjN7VAxX8bFp8RV)

