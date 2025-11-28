#!/usr/bin/env python3
"""
Script to find and replace a string in the heap of a running process
"""

import sys
import os
import re

def usage_error(message):
    """Print usage error and exit with code 1"""
    print(f"Error: {message}")
    print("Usage: read_write_heap.py pid search_string replace_string")
    print("  where pid is the pid of the running process")
    print("  and strings are ASCII")
    sys.exit(1)

def read_write_heap(pid, search_str, replace_str):
    """
    Find search_str in the heap of process pid and replace it with replace_str
    """
    if len(replace_str) > len(search_str):
        usage_error("replace_string cannot be longer than search_string")
    
    if len(replace_str) < len(search_str):
        replace_str = replace_str.ljust(len(search_str), '\x00')
    
    try:
        maps_path = f"/proc/{pid}/maps"
        with open(maps_path, 'r') as maps_file:
            maps_content = maps_file.read()
        
        heap_match = re.search(r'([0-9a-f]+)-([0-9a-f]+)\s+rw-p\s+.*\s+\[heap\]', maps_content)
        if not heap_match:
            print("Error: Could not find heap region in process memory maps")
            return False
        
        heap_start = int(heap_match.group(1), 16)
        heap_end = int(heap_match.group(2), 16)
        print(f"Found heap region: 0x{heap_start:x}-0x{heap_end:x}")
        
        mem_path = f"/proc/{pid}/mem"
        with open(mem_path, 'rb+') as mem_file:
            mem_file.seek(heap_start)
            heap_size = heap_end - heap_start
            heap_data = mem_file.read(heap_size)
            
            search_bytes = search_str.encode('ascii')
            replace_bytes = replace_str.encode('ascii')
            
            if len(replace_bytes) < len(search_bytes):
                replace_bytes = replace_bytes.ljust(len(search_bytes), b'\x00')
            
            found = False
            offset = 0
            
            while offset < len(heap_data):
                pos = heap_data.find(search_bytes, offset)
                if pos == -1:
                    break
                
                memory_address = heap_start + pos
                print(f"Found '{search_str}' at address: 0x{memory_address:x}")
                
                mem_file.seek(memory_address)
                mem_file.write(replace_bytes)
                
                print(f"Replaced with '{replace_str}'")
                found = True
                offset = pos + 1
            
            if not found:
                print(f"String '{search_str}' not found in heap")
                return False
            
            return True
            
    except PermissionError:
        print("Error: Permission denied. Try running with sudo.")
        return False
    except FileNotFoundError:
        print(f"Error: Process with PID {pid} not found")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    if len(sys.argv) != 4:
        usage_error("Wrong number of arguments")
    
    try:
        pid = int(sys.argv[1])
        search_string = sys.argv[2]
        replace_string = sys.argv[3]
    except ValueError:
        usage_error("PID must be an integer")
    
    try:
        search_string.encode('ascii')
        replace_string.encode('ascii')
    except UnicodeEncodeError:
        usage_error("Strings must be ASCII")
    
    print(f"Searching for '{search_string}' in heap of process {pid}")
    print(f"Will replace with '{replace_string}'")
    
    success = read_write_heap(pid, search_string, replace_string)
    
    if success:
        print("Operation completed successfully")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
