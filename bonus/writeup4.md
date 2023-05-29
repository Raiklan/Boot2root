# Mount squashfs

## SCP

We can scp the Boot2root iso on our kaliVM,
we open it to see what's inside,
in the casper folder we can see a filesystem.squashfs, let's try to mount it:

    sudo mount -t squashfs filesystem.squashfs /mnt

inside we can look in the root folder, let's see what's inside:

    ls -al
    total 31
    drwx------  5 root root   150 Oct 15      2015 .
    drwxrwxrwx 21 root root   352 Jun 16      2017 ..
    drwx------  2 root root    29 Oct  7      2015 .aptitude
    -rw-------  1 root root 20932 Oct 15      2015 .bash_history
    -rw-r--r--  1 root root  3106 Apr 19      2012 .bashrc
    -rw-r--r--  1 root root   140 Apr 19      2012 .profile
    -rw-r--r--  1 root root    40 Oct 15  2015     README
    -rw-------  1 root root  1024 Oct  8      2015 .rnd
    drwx------  2 root root    34 Oct  8      2015 .ssh
    drwxr-xr-x  2 root root    33 Oct 13      2015 .vim
    -rw-------  1 root root  4246 Oct 15      2015 .viminfo

We see a .bash_history, let's look at what command root used and if there are password in clear:

    cat .bash_history| grep -A1 adduser
    adduser lmezard
    vim /etc/ssh/sshd_config 
    --
    adduser postfix sasl
    vim main.cf 
    --
    man adduser
    man useradd
    --
    adduser postfix sasl
    vim /etc/default/saslauthd 
    --
    adduser
    adduser laurie
    ls
    --
    adduser thor
    ls
    --
    adduser zaz
    646da671ca01bb5d84dbb5fb2238dc8e
    --
    adduser ft_root mail
    getent group mail
    --
    adduser gmy@localhost
    adduser --force-badname gmy@localhost
    deluser gmy@localhost
    adduser --force-badname laurie@borntosec.    net
    vim /etc/squirrelmail/config.php 
    --
    adduser laurie@borntosec.net mail
    id zaz
    --
    vim 25adduser 
    ls -als
    --
    chmod 0755 25adduser 
    ls
    --
    vim 25adduser 
    ls

The only password we found is the one of ZAZ, let's try to connect to it using ssh

    ssh zaz@<Boot2Root IP>
	➜  ~ ssh zaz@<Boot2Root IP>
        ____                _______    _____           
       |  _ \              |__   __|  / ____|          
       | |_) | ___  _ __ _ __ | | ___| (___   ___  ___ 
       |  _ < / _ \| '__| '_ \| |/ _ \\___ \ / _ \/ __|
       | |_) | (_) | |  | | | | | (_) |___) |  __/ (__ 
       |____/ \___/|_|  |_| |_|_|\___/_____/ \___|\___|

                       Good luck & Have fun
	zaz@<Boot2Root IP>'s password: 
	zaz@BornToSecHackMe:~$ ls
	exploit_me  mail
	zaz@BornToSecHackMe:~$ 

Now we can use the ret2libc attack or the SHELLCODE
