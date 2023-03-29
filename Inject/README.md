## Intial Foothold
**CVE-2022-22963: Spring Cloud RCE Vulnerability**

[All about Vulnerability](https://sysdig.com/blog/cve-2022-22963-spring-cloud/)

---
### Exploit

```
python3 exploit.py
```
**What does exploit.py do**
- Create shell.sh file contains python3 onelinear reverse shell.
- Create simpleHTTPServer.
- Upload shell.sh to /tmp directory in target machine using wget.
- Run nc listener to catch reverse shell connection.
- chmod +x evil.sh, run it and get reverse shell.

