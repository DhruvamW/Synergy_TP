# Linux Commands Reference – Task 1

The commands below are documented as they behave in a standard Linux
shell (bash). Outputs shown were observed when each command was run
inside WSL installed on my system.

---

### `pwd` — print working directory

**Command:**
```bash
pwd
```
**What it does:** Prints the full path of the current working directory.

**Output observed:**
```
/home/dhruvam
```

---

### `ls` — list directory contents

**Command:**
```bash
ls
```
**What it does:** Lists the files and folders in the current directory.

**Output observed:**
```
challenge.zip      fsocity.dic  output               robots.txt
check_password.py  hash.txt     passwords.txt        server.log
ctf-journey        key          print.py             snap
drop-in            key.pub      printout.txt         sshkey.private.save
extractions        out.txt      pwn.college_Dhruvam
```

---

### `ls -la` — list all contents, long format

**Command:**
```bash
ls -la
```
**What it does:** Lists all entries (including hidden files like `.git`
and `.gitignore`) with permissions, ownership, size, and modification
date.

**Output observed:**
```
total 396
drwxr-x--- 11 dhruvam dhruvam   4096 Jun  4 14:53 .
drwxr-xr-x  3 root    root      4096 Sep 21  2025 ..
-rw-------  1 dhruvam dhruvam  17236 Jun 10 14:00 .bash_history
-rw-r--r--  1 dhruvam dhruvam    220 Sep 21  2025 .bash_logout
-rw-r--r--  1 dhruvam dhruvam   3771 Sep 21  2025 .bashrc
drwx------  2 dhruvam dhruvam   4096 Sep 21  2025 .cache
-rw-r--r--  1 dhruvam dhruvam     57 May 30 18:31 .gitconfig
drwxr-xr-x  2 dhruvam dhruvam   4096 May 30 08:57 .landscape
-rw-------  1 dhruvam dhruvam     20 Jun  4 14:53 .lesshst
drwxr-xr-x  3 dhruvam dhruvam   4096 May 28 06:39 .local
-rw-rw-r--  1 dhruvam dhruvam      0 Jun 25 06:50 .motd_shown
-rw-r--r--  1 dhruvam dhruvam    807 Sep 21  2025 .profile
drwx------  2 dhruvam dhruvam   4096 May 30 18:02 .ssh
-rw-r--r--  1 dhruvam dhruvam      0 Jan 21 16:44 .sudo_as_admin_successful
-rwxr-xr-x  1 dhruvam dhruvam  24467 Jun  4 14:50 challenge.zip
-rw-r--r--  1 dhruvam dhruvam    731 May 30 10:11 check_password.py
drwxr-xr-x  7 dhruvam dhruvam   4096 May 30 18:28 ctf-journey
drwxr-xr-x  3 dhruvam dhruvam   4096 Jun  4 14:51 drop-in
drwxr-xr-x  2 dhruvam dhruvam   4096 Jan 21 17:42 extractions
-rw-r--r--  1 dhruvam dhruvam    207 Oct  4  2025 fsocity.dic
-rw-r--r--  1 dhruvam dhruvam     41 May 30 10:03 hash.txt
-rw-------  1 dhruvam dhruvam    419 Sep 22  2025 key
-rw-r--r--  1 dhruvam dhruvam    105 Sep 22  2025 key.pub
-rw-r--r--  1 dhruvam dhruvam    315 Oct  4  2025 out.txt
-rw-r--r--  1 dhruvam dhruvam      0 May 30 09:10 output
-rw-r--r--  1 dhruvam dhruvam 142354 May 30 10:01 passwords.txt
-rw-r--r--  1 dhruvam dhruvam     16 May 31 08:37 print.py
-rw-r--r--  1 dhruvam dhruvam      0 May 30 09:09 printout.txt
drwxr-xr-x  3 dhruvam dhruvam   4096 Sep 22  2025 pwn.college_Dhruvam
-rw-r--r--  1 dhruvam dhruvam    357 Oct  4  2025 robots.txt
-rwxr-xr-x  1 dhruvam dhruvam 108322 May 30 16:07 server.log
drwx------  3 dhruvam dhruvam   4096 Jan 21 17:22 snap
-rw-r--r--  1 dhruvam dhruvam      1 May 28 06:40 sshkey.private.save
```

---

### `cd` — change directory

**Command:**
```bash
cd ctf-journey
```
**What it does:** Moves into the `ctf-journey` directory.

**Output observed:**
```
dhruvam@LAPTOP-JDVR1K5B:~/ctf-journey$
```

---

### `mkdir` — make a directory

**Command:**
```bash
mkdir demo_dir
ls
```
**What it does:** Creates a new directory.

**Output observed:**
```
challenge.zip      extractions  out.txt        pwn.college_Dhruvam
check_password.py  fsocity.dic  output         robots.txt
ctf-journey        hash.txt     passwords.txt  server.log
demo_dir           key          print.py       snap
drop-in            key.pub      printout.txt   sshkey.private.save
```

---

### `touch` — create an empty file / update timestamp

**Command:**
```bash
touch demo_dir/sample.txt
ls -la demo_dir
```
**What it does:** Creates an empty file if it doesn't exist.

**Output observed:**
```
total 8
drwxr-xr-x  2 dhruvam dhruvam 4096 Jun 25 06:53 .
drwxr-x--- 12 dhruvam dhruvam 4096 Jun 25 06:53 ..
-rw-r--r--  1 dhruvam dhruvam    0 Jun 25 06:53 sample.txt
```

---

### `echo` — print text / write text to a file

**Command:**
```bash
echo "This is a sample line for Task 1 documentation." > demo_dir/sample.txt
```
**What it does:** Prints text to the terminal, or (with `>`) writes it
into a file, overwriting existing content.

**Output observed (confirmed with `cat`):**
```
This is a sample line for Task 1 documentation.
```

---

### `cat` — display file contents

**Command:**
```bash
cat demo_dir/sample.txt
```
**What it does:** Prints the full contents of a file to the terminal.

**Output observed:**
```
This is a sample line for Task 1 documentation.
```

---

### `cp` — copy a file

**Command:**
```bash
cp demo_dir/sample.txt demo_dir/sample_copy.txt
ls -la demo_dir
```
**What it does:** Copies a file to a new location/name, leaving the
original in place.

**Output observed:**
```
total 8
drwxr-xr-x  2 dhruvam dhruvam 4096 Jun 25 06:55 .
drwxr-x--- 12 dhruvam dhruvam 4096 Jun 25 06:53 ..
-rw-r--r--  1 dhruvam dhruvam    0 Jun 25 06:53 sample.txt
-rw-r--r--  1 dhruvam dhruvam    0 Jun 25 06:55 sample_copy.txt
```

---

### `mv` — move / rename a file

**Command:**
```bash
mv demo_dir/sample_copy.txt demo_dir/sample_renamed.txt
ls demo_dir
```
**What it does:** Moves a file to a new location, or renames it if the
destination is in the same directory.

**Output observed:**
```
sample.txt  sample_renamed.txt
```

---

### `rm` — remove a file

**Command:**
```bash
rm demo_dir/sample_renamed.txt
ls demo_dir
```
**What it does:** Deletes a file permanently (no recycle bin).

**Output observed:**
```
sample.txt
```

---

### `grep` — search text inside files

**Command:**
```bash
 grep "Task 1" sample.txt
```
**What it does:** Searches a file for lines matching a pattern and
prints them.

**Output observed:**
```
This is a sample line for "Task 1" documentation.
```

---

### `find` — search for files/directories

**Command:**
```bash
~$ find -name sample.txt
```
**What it does:** Recursively searches the directory tree for files
matching a pattern.

**Output observed:**
```
./demo_dir/sample.txt
```

---

### `head` — show the first lines of a file

**Command:**
```bash
head sample.txt
```
**What it does:** Prints the first N lines of a file (default 10).

**Output observed:**
```
This is a sample line for Task 1 documentation.
```

---

### `tail` — show the last lines of a file

**Command:**
```bash
tail sample.txt
```
**What it does:** Prints the last N lines of a file (default 10).

**Output observed:**
```
This is a sample line for Task 1 documentation.
```

---

### `wc` — count lines, words, characters

**Command:**
```bash
~/demo_dir$ wc -l sample.txt
```
**What it does:** Counts lines (`-l`), words (`-w`), or
characters/bytes (`-c`) in a file. Used here with `-l` to count lines.

**Output observed:**
```
1 sample.txt
```

---
```
