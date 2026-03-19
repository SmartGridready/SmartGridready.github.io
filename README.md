# SmartGridready Online Documentation

## Manual Build

### Prepare

The project uses [virtual environments](https://docs.python.org/3/tutorial/venv.html) and [pip](https://packaging.python.org/en/latest/key_projects/#pip) to manage dependencies.

Create and/or activate virtual environment in your project directory:

```bash
python -m venv .venv

# On Linux call this:
source ./.venv/bin/activate

# On Windows call this:
.\.venv\Scripts\Activate.ps1
```

Install the necessary dependencies in your virtual environment:

```bash
pip install -U -r .\requirements.txt
```

### Build

In your virtual environment call:

```bash
make clean html
```

This will re-create the HTML documentation under `build/html`.

### Replace Content to Publish

1. Delete the complete `docs` directory from the repository root.
2. Copy everything in `build/html` into repository root and rename `html` to `docs`.
3. Check Git changes. When necessary, add new files and remove files that no longer exist.

### Publish

1. Push your changes.
2. Merge into _main_ branch. Only then is the Github pages deployment updated.

### Clean up

Deactivate virtual environment in your project directory:

```bash
deactivate
```
