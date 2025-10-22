#!/bin/bash
echo -n "$1" | openssl dgst -sha1 -hex | awk '{print $2}' > 0_hash.txt
