#!/bin/bash

# Check if argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 {xor}encoded_string"
    exit 1
fi

# Extract the base64 encoded part (remove {xor} prefix)
encoded_string="${1#\{xor\}}"

# Base64 decode the string
decoded_bytes=$(echo -n "$encoded_string" | base64 -d 2>/dev/null | od -An -tu1)

# Check if base64 decoding was successful
if [ -z "$decoded_bytes" ]; then
    echo "Error: Invalid base64 encoding or empty result"
    exit 1
fi

# XOR decode with WebSphere's default key '_' (ASCII 95)
xor_key=95
result=""

# Process each byte
for byte in $decoded_bytes; do
    # XOR the byte with the key and convert to character
    xor_val=$((byte ^ xor_key))
    result+=$(printf "\\$(printf '%03o' "$xor_val")")
done

# Output the decoded password
echo "$result"
