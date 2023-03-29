## Intial Foothold
**CVE-2022-22963: Spring Cloud RCE Vulnerability**

[All about Vulnerability](https://sysdig.com/blog/cve-2022-22963-spring-cloud/)

---
### Exploit

```
python3 exploit.py
```
**What does exploit.py do**
- Create a shell.sh file that contains a Python3 one-liner reverse shell.
- Create simple HTTP Server.
- Upload shell.sh to /tmp directory in the target machine using wget.
- Run netcat listener to catch the reverse shell connection.
- Run chmod +x evil.sh, run evil.sh and get reverse shell.

