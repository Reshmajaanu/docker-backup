#!/bin/bash
directory="$1"
file_count=$(ls -l | sed '1d' | grep -v "^d" | wc -l)

echo "Number of files in $directory: $file_count"
