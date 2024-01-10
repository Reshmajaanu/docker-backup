#!/bin/bash

# Specify the source directory
source_dir="$1"

# Create subdirectories for each file extension
for file in "$source_dir"/*; do
    if [ -f "$file" ]; then
        extension="${file##*.}"
        target_dir="$source_dir/$extension"

        # Create the subdirectory if it doesn't exist
        if [ ! -d "$target_dir" ]; then
            mkdir -p "$target_dir"
        fi

        # Move the file to the corresponding subdirectory
        mv "$file" "$target_dir/"
        echo "Moved $file to $target_dir/"
    fi
done

