#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "ERROR! not found"
fi

if test -n "$PATH"; then echo "Path is not empty"; fi

if [ -n "$PATH" ]; then echo "Again, path is not empty"; fi

line="-------------------------------------"
echo line

echo "test man"
man test
echo
