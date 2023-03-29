## Intial Foothold
- I found LFI in parameter img in url: http://10.10.11.204:8080/show_image?img=img
- I read pom.xml that contains information about the project and configuration details used by Maven to build the project. And found that project uses spring-cloud-function-web which is vulnerable to RCE.

  ![image](https://user-images.githubusercontent.com/59315492/228601971-15f3f8c9-c060-4b57-a717-7e8255e58536.png)

