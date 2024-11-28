# Finding Primes

Using distributed computing for finding all primes for a given (big) interval.

# Quick start

To run this app, first create a python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

And finally, run the app:

```bash
python src/Main.py
```

# Docker

To run using docker, you can use the following `docker run` command:

```bash
docker run --rm -v $(pwd):/app -w /app python python src/Main.py
```
