# Kottans backend

---

## 0 -- Git and GitHub

Git is a powerful tool of every developer, it makes life easier and saves time. Git simplifies work with version control, provides easy access to history of changes, it can remove fear of irreparable consequences that allow us to experiment with program, gives us opportunity to collaborate, share projects with other people and a lot more.

Course on Udacity had a great educational impact on me, a big pros that it showed different real situations and how they are handeled with Git. Were studied main concepts like commits, staging area, remote repository, branches and GitHub collaboration principles. Important idea of commiting is to understand not only how make a commit but why and how often.

*Copied from frontend course*

![Screenshot of performed tasks](task-git-intro/Udacity_Git_Screen.png)

---

## 1 - Unix Shell

Command line skills are usefull to operate with file directories, every action performed using GUI can be acomplished by line of code in CLI, this allows us to work faster and be ready to situation when graphical interface don't even exist. Also understanding of CLI is crucial to work with Git. 
Main shell tools that I've learned are:
* directory navigating commands like: pwd, ls, cd, mkdir, mv; 
* files operating commands: touch, sort, uniq, grep, sed; 
* output/input redirection commands: cat, >, >>, <, |; 
* and concept that gives us opportunity to code frequently used commands into handy scripts.

The Linux Survival tutorial introduced me a several new commands like:
* 'less' that is used for reading large file contents
* 'lpq' and 'lpqm' used to show and remove printer's queue 
* symbolic link that shows symbolic path of file location and created with 'ln' command
* 'df' command that displays free disk space 
* 'ps' command, used to examine running programs or processes 

An article on [Linux Command](http://linuxcommand.org) provided a couple useful features like Brace Expansion, Command Substitution and now I comprehend the power of `chmod 777` 😄

![Screenshot of performed tasks](task-unix-shell/CLI_Complete.png)
![Screenshot of performed tasks](task-unix-shell/Linux_Survival_Complete.png)

---

## 2 - Git Collaboration

This two completed courses, in fact, it's just repetition of earlier covered material with useful additions and some new Git features.
What was learned new: 
* Flags, that used to alter how a program functions and/or what is displayed. For example -p, --stat, --oneline, --decorate, --graph, --all for git log. This flags helps us to get more info about commits and operate with it in more convinient way;
* git show, to access info about particular commit and how it can be reached by HEAD reference;
* git tag, to label commits;
* git commit --amend, useful command to "cancel" most recent commit, allows us to add some files to staging area or change the commit message;
* git reset --soft(resets commit) --mixed(resets commit+index) --hard(resets commit+index+working area);
* git shortlog provides more clear view on commits history;
* Was introduced upstream, that helps us keep up to date our forked repository with original one;
* And at the end was reviewed powerful git rebase, that provides us ability to change past commits, for example rename, squash, delete them and lot more.   

*Copied from frontend course*

![Screenshot of performed tasks](task-git-collaboration/Version_Control_Complete.png)

![Screenshot of performed tasks](task-git-collaboration/Git_Collaboration_Complete.png)

---

## 4 - Memory Management


> What's going to happen if program reaches maximum limit of stack ?

Will occur segmentation error named stack overflow, it happens when the stack pointer exceeds the stack bound.

> What's going to happen if program requests a big (more then 128KB) memory allocation on heap ?

In Linux, will be performed anonymous memory mapping instead of using heap memory.

> What's the difference between Text and Data memory segments ?

Text memory segment is read-only and stores all of the program's code, whereas data segment holds data that may be both readable and writable and  used for static variables contents. 

<details>
  <summary>Output of `proc` command</summary>  
  
   **Heap** - [560682537000-5606825d3000]  
   **Memory Mapping Segment** - [7f8d43135000-7f8d43137000]  
   **Stack** - [7fffa75d8000-7fffa75f9000]

```md
560681596000-5606815cf000 r-xp 00000000 08:01 409093                     /usr/lib/upower/upowerd
5606817cf000-5606817d2000 r--p 00039000 08:01 409093                     /usr/lib/upower/upowerd
5606817d2000-5606817d3000 rw-p 0003c000 08:01 409093                     /usr/lib/upower/upowerd
560682537000-5606825d3000 rw-p 00000000 00:00 0                          [heap]
7f8d34000000-7f8d34021000 rw-p 00000000 00:00 0 
7f8d34021000-7f8d38000000 ---p 00000000 00:00 0 
7f8d38000000-7f8d38021000 rw-p 00000000 00:00 0 
7f8d38021000-7f8d3c000000 ---p 00000000 00:00 0 
7f8d3c000000-7f8d3c021000 rw-p 00000000 00:00 0 
7f8d3c021000-7f8d40000000 ---p 00000000 00:00 0 
7f8d40091000-7f8d40092000 ---p 00000000 00:00 0 
7f8d40092000-7f8d40892000 rw-p 00000000 00:00 0 
7f8d40892000-7f8d40893000 ---p 00000000 00:00 0 
7f8d40893000-7f8d41093000 rw-p 00000000 00:00 0 
7f8d41093000-7f8d41094000 ---p 00000000 00:00 0 
7f8d41094000-7f8d41894000 rw-p 00000000 00:00 0 
7f8d41894000-7f8d41895000 ---p 00000000 00:00 0 
7f8d41895000-7f8d42095000 rw-p 00000000 00:00 0 
7f8d42095000-7f8d43131000 r--p 00000000 08:01 404792                     /usr/lib/locale/locale-archive
7f8d43131000-7f8d43135000 rw-p 00000000 00:00 0 
7f8d43135000-7f8d43137000 r--p 00000000 08:01 1054422                    /lib/x86_64-linux-gnu/libuuid.so.1.3.0
7f8d43137000-7f8d4313b000 r-xp 00002000 08:01 1054422                    /lib/x86_64-linux-gnu/libuuid.so.1.3.0
7f8d4313b000-7f8d4313c000 r--p 00006000 08:01 1054422                    /lib/x86_64-linux-gnu/libuuid.so.1.3.0
7f8d4313c000-7f8d4313d000 r--p 00006000 08:01 1054422                    /lib/x86_64-linux-gnu/libuuid.so.1.3.0
7f8d4313d000-7f8d4313e000 rw-p 00007000 08:01 1054422                    /lib/x86_64-linux-gnu/libuuid.so.1.3.0
7f8d4313e000-7f8d4315c000 r-xp 00000000 08:01 1054352                    /lib/x86_64-linux-gnu/libgpg-error.so.0.24.3
7f8d4315c000-7f8d4335c000 ---p 0001e000 08:01 1054352                    /lib/x86_64-linux-gnu/libgpg-error.so.0.24.3
7f8d4335c000-7f8d4335d000 r--p 0001e000 08:01 1054352                    /lib/x86_64-linux-gnu/libgpg-error.so.0.24.3
7f8d4335d000-7f8d4335e000 rw-p 0001f000 08:01 1054352                    /lib/x86_64-linux-gnu/libgpg-error.so.0.24.3
7f8d4335e000-7f8d433dd000 r-xp 00000000 08:01 409548                     /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.2
7f8d433dd000-7f8d435dd000 ---p 0007f000 08:01 409548                     /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.2
7f8d435dd000-7f8d435de000 r--p 0007f000 08:01 409548                     /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.2
7f8d435de000-7f8d435df000 rw-p 00080000 08:01 409548                     /usr/lib/x86_64-linux-gnu/libgmp.so.10.3.2
7f8d435df000-7f8d43612000 r-xp 00000000 08:01 409604                     /usr/lib/x86_64-linux-gnu/libhogweed.so.4.4
7f8d43612000-7f8d43811000 ---p 00033000 08:01 409604                     /usr/lib/x86_64-linux-gnu/libhogweed.so.4.4
7f8d43811000-7f8d43812000 r--p 00032000 08:01 409604                     /usr/lib/x86_64-linux-gnu/libhogweed.so.4.4
7f8d43812000-7f8d43813000 rw-p 00033000 08:01 409604                     /usr/lib/x86_64-linux-gnu/libhogweed.so.4.4
7f8d43813000-7f8d43815000 rw-p 00000000 00:00 0 

7f8d43815000-7f8d43849000 r-xp 00000000 08:01 409745                     /usr/lib/x86_64-linux-gnu/libnettle.so.6.4
7f8d43849000-7f8d43a48000 ---p 00034000 08:01 409745                     /usr/lib/x86_64-linux-gnu/libnettle.so.6.4
7f8d43a48000-7f8d43a4a000 r--p 00033000 08:01 409745                     /usr/lib/x86_64-linux-gnu/libnettle.so.6.4
7f8d43a4a000-7f8d43a4b000 rw-p 00035000 08:01 409745                     /usr/lib/x86_64-linux-gnu/libnettle.so.6.4
7f8d43a4b000-7f8d43a5b000 r--p 00000000 08:01 409939                     /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
7f8d43a5b000-7f8d43a8f000 r-xp 00010000 08:01 409939                     /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
7f8d43a8f000-7f8d43bc6000 r--p 00044000 08:01 409939                     /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
7f8d43bc6000-7f8d43bc7000 ---p 0017b000 08:01 409939                     /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
7f8d43bc7000-7f8d43bca000 r--p 0017b000 08:01 409939                     /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
7f8d43bca000-7f8d43bcb000 rw-p 0017e000 08:01 409939                     /usr/lib/x86_64-linux-gnu/libunistring.so.2.1.0
7f8d43bcb000-7f8d43bcd000 r--p 00000000 08:01 409626                     /usr/lib/x86_64-linux-gnu/libidn2.so.0.3.4
7f8d43bcd000-7f8d43bd1000 r-xp 00002000 08:01 409626                     /usr/lib/x86_64-linux-gnu/libidn2.so.0.3.4
7f8d43bd1000-7f8d43be8000 r--p 00006000 08:01 409626                     /usr/lib/x86_64-linux-gnu/libidn2.so.0.3.4
7f8d43be8000-7f8d43be9000 r--p 0001c000 08:01 409626                     /usr/lib/x86_64-linux-gnu/libidn2.so.0.3.4
7f8d43be9000-7f8d43bea000 rw-p 0001d000 08:01 409626                     /usr/lib/x86_64-linux-gnu/libidn2.so.0.3.4
7f8d43bea000-7f8d43c15000 r--p 00000000 08:01 409775                     /usr/lib/x86_64-linux-gnu/libp11-kit.so.0.3.0
7f8d43c15000-7f8d43ca9000 r-xp 0002b000 08:01 409775                     /usr/lib/x86_64-linux-gnu/libp11-kit.so.0.3.0
7f8d43ca9000-7f8d43d04000 r--p 000bf000 08:01 409775                     /usr/lib/x86_64-linux-gnu/libp11-kit.so.0.3.0
7f8d43d04000-7f8d43d05000 ---p 0011a000 08:01 409775                     /usr/lib/x86_64-linux-gnu/libp11-kit.so.0.3.0
7f8d43d05000-7f8d43d0f000 r--p 0011a000 08:01 409775                     /usr/lib/x86_64-linux-gnu/libp11-kit.so.0.3.0
7f8d43d0f000-7f8d43d19000 rw-p 00124000 08:01 409775                     /usr/lib/x86_64-linux-gnu/libp11-kit.so.0.3.0
7f8d43d19000-7f8d43d1b000 r--p 00000000 08:01 1054408                    /lib/x86_64-linux-gnu/librt-2.28.so
7f8d43d1b000-7f8d43d1f000 r-xp 00002000 08:01 1054408                    /lib/x86_64-linux-gnu/librt-2.28.so
7f8d43d1f000-7f8d43d21000 r--p 00006000 08:01 1054408                    /lib/x86_64-linux-gnu/librt-2.28.so
7f8d43d21000-7f8d43d22000 r--p 00007000 08:01 1054408                    /lib/x86_64-linux-gnu/librt-2.28.so
7f8d43d22000-7f8d43d23000 rw-p 00008000 08:01 1054408                    /lib/x86_64-linux-gnu/librt-2.28.so
7f8d43d23000-7f8d43d2d000 r--p 00000000 08:01 1054330                    /lib/x86_64-linux-gnu/libblkid.so.1.1.0
7f8d43d2d000-7f8d43d5e000 r-xp 0000a000 08:01 1054330                    /lib/x86_64-linux-gnu/libblkid.so.1.1.0
7f8d43d5e000-7f8d43d6e000 r--p 0003b000 08:01 1054330                    /lib/x86_64-linux-gnu/libblkid.so.1.1.0
7f8d43d6e000-7f8d43d72000 r--p 0004a000 08:01 1054330                    /lib/x86_64-linux-gnu/libblkid.so.1.1.0
7f8d43d72000-7f8d43d73000 rw-p 0004e000 08:01 1054330                    /lib/x86_64-linux-gnu/libblkid.so.1.1.0
7f8d43d73000-7f8d43d76000 rw-p 00000000 00:00 0 
7f8d43d76000-7f8d43d77000 r--p 00000000 08:01 1054343                    /lib/x86_64-linux-gnu/libdl-2.28.so
7f8d43d77000-7f8d43d79000 r-xp 00001000 08:01 1054343                    /lib/x86_64-linux-gnu/libdl-2.28.so
7f8d43d79000-7f8d43d7a000 r--p 00003000 08:01 1054343                    /lib/x86_64-linux-gnu/libdl-2.28.so
7f8d43d7a000-7f8d43d7b000 r--p 00003000 08:01 1054343                    /lib/x86_64-linux-gnu/libdl-2.28.so
7f8d43d7b000-7f8d43d7c000 rw-p 00004000 08:01 1054343                    /lib/x86_64-linux-gnu/libdl-2.28.so
7f8d43d7c000-7f8d43d83000 r-xp 00000000 08:01 409946                     /usr/lib/x86_64-linux-gnu/libusbmuxd.so.4.0.0
7f8d43d83000-7f8d43f82000 ---p 00007000 08:01 409946                     /usr/lib/x86_64-linux-gnu/libusbmuxd.so.4.0.0
7f8d43f82000-7f8d43f83000 r--p 00006000 08:01 409946                     /usr/lib/x86_64-linux-gnu/libusbmuxd.so.4.0.0
7f8d43f83000-7f8d43f84000 rw-p 00007000 08:01 409946                     /usr/lib/x86_64-linux-gnu/libusbmuxd.so.4.0.0
7f8d43f84000-7f8d44099000 r-xp 00000000 08:01 1054351                    /lib/x86_64-linux-gnu/libgcrypt.so.20.2.3
7f8d44099000-7f8d44298000 ---p 00115000 08:01 1054351                    /lib/x86_64-linux-gnu/libgcrypt.so.20.2.3
7f8d44298000-7f8d4429a000 r--p 00114000 08:01 1054351                    /lib/x86_64-linux-gnu/libgcrypt.so.20.2.3
7f8d4429a000-7f8d4429f000 rw-p 00116000 08:01 1054351                    /lib/x86_64-linux-gnu/libgcrypt.so.20.2.3
7f8d4429f000-7f8d442a0000 rw-p 00000000 00:00 0 
7f8d442a0000-7f8d442b1000 r-xp 00000000 08:01 409917                     /usr/lib/x86_64-linux-gnu/libtasn1.so.6.5.5
7f8d442b1000-7f8d444b1000 ---p 00011000 08:01 409917                     /usr/lib/x86_64-linux-gnu/libtasn1.so.6.5.5
7f8d444b1000-7f8d444b2000 r--p 00011000 08:01 409917                     /usr/lib/x86_64-linux-gnu/libtasn1.so.6.5.5
7f8d444b2000-7f8d444b3000 rw-p 00012000 08:01 409917                     /usr/lib/x86_64-linux-gnu/libtasn1.so.6.5.5
7f8d444b3000-7f8d444df000 r--p 00000000 08:01 408310                     /usr/lib/x86_64-linux-gnu/libgnutls.so.30.22.0
7f8d444df000-7f8d445da000 r-xp 0002c000 08:01 408310                     /usr/lib/x86_64-linux-gnu/libgnutls.so.30.22.0
7f8d445da000-7f8d4463e000 r--p 00127000 08:01 408310                     /usr/lib/x86_64-linux-gnu/libgnutls.so.30.22.0
7f8d4463e000-7f8d4464d000 r--p 0018a000 08:01 408310                     /usr/lib/x86_64-linux-gnu/libgnutls.so.30.22.0
7f8d4464d000-7f8d4464e000 rw-p 00199000 08:01 408310                     /usr/lib/x86_64-linux-gnu/libgnutls.so.30.22.0
7f8d4464e000-7f8d44651000 rw-p 00000000 00:00 0 
7f8d44651000-7f8d44653000 r--p 00000000 08:01 1054398                    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
7f8d44653000-7f8d446a5000 r-xp 00002000 08:01 1054398                    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
7f8d446a5000-7f8d446c3000 r--p 00054000 08:01 1054398                    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
7f8d446c3000-7f8d446c4000 r--p 00071000 08:01 1054398                    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
7f8d446c4000-7f8d446c5000 rw-p 00072000 08:01 1054398                    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
7f8d446c5000-7f8d446cc000 r-xp 00000000 08:01 409483                     /usr/lib/x86_64-linux-gnu/libffi.so.6.0.4
7f8d446cc000-7f8d448cb000 ---p 00007000 08:01 409483                     /usr/lib/x86_64-linux-gnu/libffi.so.6.0.4
7f8d448cb000-7f8d448cc000 r--p 00006000 08:01 409483                     /usr/lib/x86_64-linux-gnu/libffi.so.6.0.4
7f8d448cc000-7f8d448cd000 rw-p 00007000 08:01 409483                     /usr/lib/x86_64-linux-gnu/libffi.so.6.0.4
7f8d448cd000-7f8d448d1000 r--p 00000000 08:01 1049289                    /lib/x86_64-linux-gnu/libudev.so.1.6.11
7f8d448d1000-7f8d448e4000 r-xp 00004000 08:01 1049289                    /lib/x86_64-linux-gnu/libudev.so.1.6.11
7f8d448e4000-7f8d448eb000 r--p 00017000 08:01 1049289                    /lib/x86_64-linux-gnu/libudev.so.1.6.11
7f8d448eb000-7f8d448ec000 r--p 0001d000 08:01 1049289                    /lib/x86_64-linux-gnu/libudev.so.1.6.11
7f8d448ec000-7f8d448ed000 rw-p 0001e000 08:01 1049289                    /lib/x86_64-linux-gnu/libudev.so.1.6.11
7f8d448ed000-7f8d448f8000 r--p 00000000 08:01 1054368                    /lib/x86_64-linux-gnu/libmount.so.1.1.0
7f8d448f8000-7f8d44930000 r-xp 0000b000 08:01 1054368                    /lib/x86_64-linux-gnu/libmount.so.1.1.0
7f8d44930000-7f8d44942000 r--p 00043000 08:01 1054368                    /lib/x86_64-linux-gnu/libmount.so.1.1.0
7f8d44942000-7f8d44944000 r--p 00054000 08:01 1054368                    /lib/x86_64-linux-gnu/libmount.so.1.1.0
7f8d44944000-7f8d44945000 rw-p 00056000 08:01 1054368                    /lib/x86_64-linux-gnu/libmount.so.1.1.0
7f8d44945000-7f8d44946000 rw-p 00000000 00:00 0 
7f8d44946000-7f8d4494a000 r--p 00000000 08:01 1054407                    /lib/x86_64-linux-gnu/libresolv-2.28.so
7f8d4494a000-7f8d44959000 r-xp 00004000 08:01 1054407                    /lib/x86_64-linux-gnu/libresolv-2.28.so
7f8d44959000-7f8d4495d000 r--p 00013000 08:01 1054407                    /lib/x86_64-linux-gnu/libresolv-2.28.so
7f8d4495d000-7f8d4495e000 r--p 00016000 08:01 1054407                    /lib/x86_64-linux-gnu/libresolv-2.28.so
7f8d4495e000-7f8d4495f000 rw-p 00017000 08:01 1054407                    /lib/x86_64-linux-gnu/libresolv-2.28.so
7f8d4495f000-7f8d44961000 rw-p 00000000 00:00 0 
7f8d44961000-7f8d44986000 r-xp 00000000 08:01 1054409                    /lib/x86_64-linux-gnu/libselinux.so.1
7f8d44986000-7f8d44b85000 ---p 00025000 08:01 1054409                    /lib/x86_64-linux-gnu/libselinux.so.1
7f8d44b85000-7f8d44b86000 r--p 00024000 08:01 1054409                    /lib/x86_64-linux-gnu/libselinux.so.1
7f8d44b86000-7f8d44b87000 rw-p 00025000 08:01 1054409                    /lib/x86_64-linux-gnu/libselinux.so.1
7f8d44b87000-7f8d44b8b000 rw-p 00000000 00:00 0 
7f8d44b8b000-7f8d44ba7000 r-xp 00000000 08:01 1054424                    /lib/x86_64-linux-gnu/libz.so.1.2.11
7f8d44ba7000-7f8d44da6000 ---p 0001c000 08:01 1054424                    /lib/x86_64-linux-gnu/libz.so.1.2.11
7f8d44da6000-7f8d44da7000 r--p 0001b000 08:01 1054424                    /lib/x86_64-linux-gnu/libz.so.1.2.11
7f8d44da7000-7f8d44da8000 rw-p 0001c000 08:01 1054424                    /lib/x86_64-linux-gnu/libz.so.1.2.11
7f8d44da8000-7f8d44dae000 r--p 00000000 08:01 1054404                    /lib/x86_64-linux-gnu/libpthread-2.28.so
7f8d44dae000-7f8d44dbd000 r-xp 00006000 08:01 1054404                    /lib/x86_64-linux-gnu/libpthread-2.28.so
7f8d44dbd000-7f8d44dc3000 r--p 00015000 08:01 1054404                    /lib/x86_64-linux-gnu/libpthread-2.28.so
7f8d44dc3000-7f8d44dc4000 r--p 0001a000 08:01 1054404                    /lib/x86_64-linux-gnu/libpthread-2.28.so
7f8d44dc4000-7f8d44dc5000 rw-p 0001b000 08:01 1054404                    /lib/x86_64-linux-gnu/libpthread-2.28.so
7f8d44dc5000-7f8d44dc9000 rw-p 00000000 00:00 0 
7f8d44dc9000-7f8d44dca000 r--p 00000000 08:01 396434                     /usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0.5800.1
7f8d44dca000-7f8d44dcc000 r-xp 00001000 08:01 396434                     /usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0.5800.1
7f8d44dcc000-7f8d44dcd000 r--p 00003000 08:01 396434                     /usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0.5800.1
7f8d44dcd000-7f8d44dce000 r--p 00003000 08:01 396434                     /usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0.5800.1
7f8d44dce000-7f8d44dcf000 rw-p 00004000 08:01 396434                     /usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0.5800.1
7f8d44dcf000-7f8d44df1000 r--p 00000000 08:01 1054333                    /lib/x86_64-linux-gnu/libc-2.28.so
7f8d44df1000-7f8d44f62000 r-xp 00022000 08:01 1054333                    /lib/x86_64-linux-gnu/libc-2.28.so
7f8d44f62000-7f8d44fae000 r--p 00193000 08:01 1054333                    /lib/x86_64-linux-gnu/libc-2.28.so
7f8d44fae000-7f8d44faf000 ---p 001df000 08:01 1054333                    /lib/x86_64-linux-gnu/libc-2.28.so
7f8d44faf000-7f8d44fb3000 r--p 001df000 08:01 1054333                    /lib/x86_64-linux-gnu/libc-2.28.so
7f8d44fb3000-7f8d44fb5000 rw-p 001e3000 08:01 1054333                    /lib/x86_64-linux-gnu/libc-2.28.so
7f8d44fb5000-7f8d44fb9000 rw-p 00000000 00:00 0 
7f8d44fb9000-7f8d44fbb000 r--p 00000000 08:01 409807                     /usr/lib/x86_64-linux-gnu/libplist.so.3.1.0
7f8d44fbb000-7f8d44fc4000 r-xp 00002000 08:01 409807                     /usr/lib/x86_64-linux-gnu/libplist.so.3.1.0
7f8d44fc4000-7f8d44fc7000 r--p 0000b000 08:01 409807                     /usr/lib/x86_64-linux-gnu/libplist.so.3.1.0
7f8d44fc7000-7f8d44fc8000 r--p 0000d000 08:01 409807                     /usr/lib/x86_64-linux-gnu/libplist.so.3.1.0
7f8d44fc8000-7f8d44fc9000 rw-p 0000e000 08:01 409807                     /usr/lib/x86_64-linux-gnu/libplist.so.3.1.0
7f8d44fc9000-7f8d44feb000 r-xp 00000000 08:01 409630                     /usr/lib/x86_64-linux-gnu/libimobiledevice.so.6.0.0
7f8d44feb000-7f8d451ea000 ---p 00022000 08:01 409630                     /usr/lib/x86_64-linux-gnu/libimobiledevice.so.6.0.0
7f8d451ea000-7f8d451eb000 r--p 00021000 08:01 409630                     /usr/lib/x86_64-linux-gnu/libimobiledevice.so.6.0.0
7f8d451eb000-7f8d451ec000 rw-p 00022000 08:01 409630                     /usr/lib/x86_64-linux-gnu/libimobiledevice.so.6.0.0
7f8d451ec000-7f8d451ee000 rw-p 00000000 00:00 0 
7f8d451ee000-7f8d45209000 r--p 00000000 08:01 396432                     /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0.5800.1
7f8d45209000-7f8d45286000 r-xp 0001b000 08:01 396432                     /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0.5800.1
7f8d45286000-7f8d45308000 r--p 00098000 08:01 396432                     /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0.5800.1
7f8d45308000-7f8d45309000 r--p 00119000 08:01 396432                     /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0.5800.1
7f8d45309000-7f8d4530a000 rw-p 0011a000 08:01 396432                     /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0.5800.1
7f8d4530a000-7f8d4530b000 rw-p 00000000 00:00 0 
7f8d4530b000-7f8d45316000 r--p 00000000 08:01 396833                     /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0.5800.1
7f8d45316000-7f8d45347000 r-xp 0000b000 08:01 396833                     /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0.5800.1
7f8d45347000-7f8d4535d000 r--p 0003c000 08:01 396833                     /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0.5800.1
7f8d4535d000-7f8d4535e000 r--p 00051000 08:01 396833                     /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0.5800.1
7f8d4535e000-7f8d4535f000 rw-p 00052000 08:01 396833                     /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0.5800.1
7f8d4535f000-7f8d45368000 r-xp 00000000 08:01 409594                     /usr/lib/x86_64-linux-gnu/libgudev-1.0.so.0.2.0
7f8d45368000-7f8d45567000 ---p 00009000 08:01 409594                     /usr/lib/x86_64-linux-gnu/libgudev-1.0.so.0.2.0
7f8d45567000-7f8d45568000 r--p 00008000 08:01 409594                     /usr/lib/x86_64-linux-gnu/libgudev-1.0.so.0.2.0
7f8d45568000-7f8d45569000 rw-p 00009000 08:01 409594                     /usr/lib/x86_64-linux-gnu/libgudev-1.0.so.0.2.0
7f8d45569000-7f8d45580000 r-xp 00000000 08:01 1054420                    /lib/x86_64-linux-gnu/libusb-1.0.so.0.1.0
7f8d45580000-7f8d45780000 ---p 00017000 08:01 1054420                    /lib/x86_64-linux-gnu/libusb-1.0.so.0.1.0
7f8d45780000-7f8d45781000 r--p 00017000 08:01 1054420                    /lib/x86_64-linux-gnu/libusb-1.0.so.0.1.0
7f8d45781000-7f8d45782000 rw-p 00018000 08:01 1054420                    /lib/x86_64-linux-gnu/libusb-1.0.so.0.1.0
7f8d45782000-7f8d457b7000 r--p 00000000 08:01 396430                     /usr/lib/x86_64-linux-gnu/libgio-2.0.so.0.5800.1
7f8d457b7000-7f8d458a0000 r-xp 00035000 08:01 396430                     /usr/lib/x86_64-linux-gnu/libgio-2.0.so.0.5800.1
7f8d458a0000-7f8d4591c000 r--p 0011e000 08:01 396430                     /usr/lib/x86_64-linux-gnu/libgio-2.0.so.0.5800.1
7f8d4591c000-7f8d4591d000 ---p 0019a000 08:01 396430                     /usr/lib/x86_64-linux-gnu/libgio-2.0.so.0.5800.1
7f8d4591d000-7f8d45924000 r--p 0019a000 08:01 396430                     /usr/lib/x86_64-linux-gnu/libgio-2.0.so.0.5800.1
7f8d45924000-7f8d45925000 rw-p 001a1000 08:01 396430                     /usr/lib/x86_64-linux-gnu/libgio-2.0.so.0.5800.1
7f8d45925000-7f8d45927000 rw-p 00000000 00:00 0 
7f8d45927000-7f8d4594b000 r-xp 00000000 08:01 409945                     /usr/lib/x86_64-linux-gnu/libupower-glib.so.3.0.1
7f8d4594b000-7f8d45b4b000 ---p 00024000 08:01 409945                     /usr/lib/x86_64-linux-gnu/libupower-glib.so.3.0.1
7f8d45b4b000-7f8d45b4d000 r--p 00024000 08:01 409945                     /usr/lib/x86_64-linux-gnu/libupower-glib.so.3.0.1
7f8d45b4d000-7f8d45b4e000 rw-p 00026000 08:01 409945                     /usr/lib/x86_64-linux-gnu/libupower-glib.so.3.0.1
7f8d45b4e000-7f8d45b50000 rw-p 00000000 00:00 0 
7f8d45b63000-7f8d45b6a000 r--s 00000000 08:01 527101                     /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache
7f8d45b6a000-7f8d45b6b000 r--p 00000000 08:01 1054321                    /lib/x86_64-linux-gnu/ld-2.28.so
7f8d45b6b000-7f8d45b8b000 r-xp 00001000 08:01 1054321                    /lib/x86_64-linux-gnu/ld-2.28.so
7f8d45b8b000-7f8d45b93000 r--p 00021000 08:01 1054321                    /lib/x86_64-linux-gnu/ld-2.28.so
7f8d45b93000-7f8d45b94000 r--p 00028000 08:01 1054321                    /lib/x86_64-linux-gnu/ld-2.28.so
7f8d45b94000-7f8d45b95000 rw-p 00029000 08:01 1054321                    /lib/x86_64-linux-gnu/ld-2.28.so
7f8d45b95000-7f8d45b96000 rw-p 00000000 00:00 0 

7fffa75d8000-7fffa75f9000 rw-p 00000000 00:00 0                          [stack]
7fffa75fb000-7fffa75fe000 r--p 00000000 00:00 0                          [vvar]
7fffa75fe000-7fffa7600000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
```
</details>

The article explains basics of memory management, reveals concept of virtual adresses and describes roles of diffent memory segments. It's important to keep in mind problems that can occur beacause of stack or heap expanding.

---

## 5 - TCP. UDP. Network

**Internet 101** videos are extremely teachable and information presented in nice-looking form, good for me I'm aldready familiar with terminilogy of Internet and TCP/IP protocols (thanks NAU, very cool). 

**How DNS Works**. Education in the form of comics? yes please. In entertaining form it explains how DNS works and what a journey lies behind a DNS query. Main concepts that I learned is that every unit in this DNS-finding sequence doesn't need to know every address in the Internet, it just knows where to ask, and another thing that helps is cash where machine can look before asking.
**Networking for Web Developers**
TCP flag is a part of the TCP packet and used to communicate between sender and receiver in the form of boolean value.
I find this familiar to the conversation of two people with walkie-talkie. They need some code prhases to signal start or end of conversation, acknowledgment of data delivery like [S],[F] and [.] flags in TCP packet. 
traceroute - tell us how many hops are between you and destination address.
ttl - time to live

Firewall is one of the **middlebox** devices that performs filtering function between client and server, it can also change traffic, e.g. replace content of a web-page in politic or social purposes.
NAT is another example of middlebox devices, they act as a bridge between outside and inside network, several devices in local network can share the same "outside" address, usually our home routers perform both firewall and NAT functions.  

![Screenshot of performed tasks](task-networks/udacity-networking-complete.png)