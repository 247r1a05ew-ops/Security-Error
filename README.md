# Security Issue Demo

This project demonstrates detection of a hard-coded secret.

The API key is intentionally written directly inside the source code.

## Expected

BUILD -> PASS
TESTS -> PASS
SECURITY -> WARNING/FAIL

## Fix

Do not store credentials directly in source code.

Use an environment variable instead.

Example:

API_KEY = os.environ.get("API_KEY")
