"""
TextParser - Extracts ERROR messages from a log file,
removes timestamps, and prints clean error messages.
"""

import re
import sys
from typing import List


class TextParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_errors(self) -> List[str]:
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()

            error_messages = []
            for line in lines:
                if "ERROR" in line:
                    # Remove timestamp and "ERROR" label using regex
                    match = re.search(r'ERROR (.+)', line)
                    if match:
                        error_messages.append(match.group(1).strip())
            return error_messages

        except FileNotFoundError:
            raise FileNotFoundError(f"Log file '{self.file_path}' not found.")
        except Exception as e:
            raise Exception(f"An error occurred while parsing: {e}")

    def print_errors(self):
        errors = self.extract_errors()
        print("Extracted ERROR messages:")
        for err in errors:
            print(err)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python text_parser.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]
    parser = TextParser(log_file)
    parser.print_errors()
