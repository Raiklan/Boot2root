# Boot2root
##  Goal of the project
We have an ISO file given to us, the goal is to become root on that iso, we cannot use grub, so we have to find other ways ! [See the subject right here.](https://github.com/Raiklan/Boot2root/blob/main/en.subject-9.pdf)
 
## Summary
|Writeup|Exploit| Documentation|
|--|--|--|
| [1](https://github.com/Raiklan/Boot2root/blob/main/writeup1.md) |SQL injection, Ret2libc| [Ret2libc](https://www.ired.team/offensive-security/code-injection-process-injection/binary-exploitation/return-to-libc-ret2libc)|
| [2](https://github.com/Raiklan/Boot2root/blob/main/writeup2.md) | Reverse Shell, Dirty COW | [Dirty COW](https://dirtycow.ninja) |
|3 | suEXEC Apache 2.2 | [suExec](https://www.exploit-db.com/exploits/27397) |
|4 | Analyzing filesystem.squashfs | [Mount Squashfs file](https://askubuntu.com/questions/437880/extract-a-squashfs-to-an-existing-directory) |
|5| Shellcode injection in bufferoverflow | [Shellcode](https://shell-storm.org/shellcode/files/shellcode-885.html)
