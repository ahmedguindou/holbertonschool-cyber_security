#!/bin/bash
curl -s -X POST -H "Host: $1" -d "$3" "$2" | grep -q "$1" && printf ok || printf invalid
