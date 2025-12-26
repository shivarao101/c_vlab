#!/bin/bash

gcc program.c -o program -lm 2> compile_error.txt

if [ $? -ne 0 ]; then
    cat compile_error.txt
    exit 1
fi

./program < input.txt > output.txt
cat output.txt
