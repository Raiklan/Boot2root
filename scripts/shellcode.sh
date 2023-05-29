#!/bin/bash

echo 'void main(){printf("%p\n", getenv("SHELLCODE"));}' > /tmp/getenv.c
gcc /tmp/getenv.c -o /tmp/shellcode
chmod 777 /tmp/shellcode
/tmp/shellcode 
