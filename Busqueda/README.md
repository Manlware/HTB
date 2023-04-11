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
 - I found that eval function take string and run it as python code I tried it and it worked. 
  ![image](https://user-images.githubusercontent.com/59315492/230914598-544158e0-615f-4717-a17e-c004e5acd936.png)
  ![image](https://user-images.githubusercontent.com/59315492/230914677-8a5643a9-ba84-44ed-94df-bc6828463364.png)
 - I found way to get RCE using eval in [Bypass python sandbox](https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes)
  ![image](https://user-images.githubusercontent.com/59315492/230915451-e15ea78f-60fc-4d4d-903c-4f03ba152e02.png)
  ![image](https://user-images.githubusercontent.com/59315492/230915542-36152379-2e8e-4a13-b92a-602d13a1c5cf.png)
 
 - Finally I wrote python code to exploit it and get shell. 

---
## Privilege Escalation:
**Use sudo -l and use python3 /opt/scripts/system-checkup.py to get root**
### Exploit

- I found svc password in ``/var/www/app/.git/config`` file and used it to ssh.
- Run sudo -l and found that we can run ``/usr/bin/python3 /opt/scripts/system-checkup.py *`` using sudo.
- I cd to ``/opt/scripts/`` and run the command ``sudo /usr/bin/python3 /opt/scripts/system-checkup.py`` and found that is has 3 args docker-ps, docker-inspect and full-checkup and I tried all of them and found that full-checkup run a file locate in the same directory called full-checkup.sh.
- So I cd to /tmp and create file called ``full-checkup.sh`` that contain simple command id and ``chmod +x full-checkup.sh`` and run ``sudo /usr/bin/python3 /opt/scripts/system-checkup.py full-check``upand now I am root.
![image](https://user-images.githubusercontent.com/59315492/231019258-1e9834d7-ab03-439b-a14f-c7dc892c0366.png)

### Python Automation Exploit:
**Steps:**
- Download PrivEsc.py script on target machine
- Run it and now you are root!
```
  python3 PrivEsc.py
```
![image](https://user-images.githubusercontent.com/59315492/231023082-df3988c8-9668-4080-aeb2-647524bfcff2.png)


