#!/bin/bash

INPUT_FILE="sample.log"

if [[ ! -f $INPUT_FILE ]]; then
  echo "Log file '$INPUT_FILE' not found."
  exit 1
fi

echo "Extracted ERROR messages:"
grep "ERROR" "$INPUT_FILE" | sed -E 's/^[0-9:\- ]+ERROR //'
