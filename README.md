# api-fuzzer

This is a Python script that processes words input via `stdin` by sending 
them to a specified API endpoint and handles the response accordingly.

It works with the `requests` library and can handle both successful responses 
(status code 200) and redirections (status code 307).

## Features:

- Takes input via `stdin` and processes each word.
- Sends requests to an API endpoint.
- Handles both JSON responses and plain text responses.
- Handles HTTP redirections (status code 307).

## Requirements:

- Python 3.x
- `requests` library (install via `pip`)

## Installation:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/word-api-processor.git
   cd word-api-processor
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. If you don't have a requirements.txt file yet, create one with the
   following content:
   ```bash
   sudo nano requirements.txt
   ```
   requests

## Usage

   ```bash
   cat <wordlist> | python3 fuzzer.py
   ```

## License

This project is licensed under the MIT license.
