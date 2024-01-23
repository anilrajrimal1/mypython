# Project 3: CI/CD Setup with GitHub, Jenkins, and Apache Webserver(Python Based)

## Overview

This project focuses on setting up a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub, Jenkins, and an Apache Webserver. The primary objectives include configuring Jenkins, Git, and Apache Webserver, integrating GitHub with Jenkins and Apache, creating CI and CD jobs, and testing the deployment of a Python-based website.


developers --->push--> Git hub --->pull-->Jenkins -->pipeline - build --> webserver (Apache)

# Table of Contents

1. [Installing Apache Server in Webserver and Configuring to Host Python-Based Webpage](#1-installing-apache-server-in-webserver-and-configuring-to-host-python-based-webpage)
2. [Creating a New Repo in GitHub for Our Python-Based Website](#2-creating-a-new-repo-in-github-for-our-python-based-website)
3. [Creating a Job in Jenkins to Pull index.wsgi from the GitHub Repo and Send it to the Web Server in /var/www/html Directory](#3-creating-a-job-in-jenkins-to-pull-indexwsgi-from-the-github-repo-and-send-it-to-the-web-server-in-varwwwhtml-directory)
## 1. Installing Apache Server in Webserver and Configuring to Host Python-Based Webpage

To set up the Apache server and Python on your webserver, follow the steps below:

- Install Apache server and Python:
   ```bash
   # Install Apache and Python
   sudo yum -y install httpd mod_wsgi

    ```
![install-python](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/install%20httpd%20and%20python%20on%20Anil.png)

- Start the Apache service:
   ```bash
   # Start the Apache service
    sudo systemctl start httpd
   
    ```

- Enable the Apache service to start on boot:
   ```bash
   # Enable Apache service for startup
    sudo systemctl enable httpd 
    sudo systemctl status httpd
    ```
![status-httpd](https://github.com/anilrajrimal1/myhtml/blob/master/screenshots/httpd%20status.png)

- Add the HTTP service to the firewall (permanent):
   ```bash
   # Add HTTP port to firewall
    sudo firewall-cmd --permanent --add-service=http
    ```

- Reload the firewall to apply changes:
   ```bash
   # Reload the firewall
    sudo firewall-cmd --reload

    ```
![firewall](https://github.com/anilrajrimal1/myhtml/blob/master/screenshots/firewall%20port.png)

- Configuring webserver for python-based webpage
   ```bash
  cd /etc/httpd/conf.d
    ```

  ```bash
  ls
  ```

   ```bash
	vi python.conf

  ```
  ![conf-host](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/python%20conf.png)

  #set this to python.conf
	<VirtualHost *:80>
	WSGIScriptAlias	/	/var/www/html/index.wsgi
	</VirtualHost>

  ```bash
	systemctl reload httpd
  ```
These commands will install Apache server and Python, start the Apache service, enable it for startup, and configure the firewall to allow HTTP traffic.

## 2. Creating a New Repo in GitHub for Our Python-Based Website
To create a new GitHub repository for our Python project and initialize it locally, follow the steps below:

### Login to GitHub:
   - Create a new repository named "mypython".
   - Copy the repository URL.

![create-repo](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/create%20mypython%20repo.png)

- On your developer's machine, power on and create a folder for your project:
   ```bash
   # Create project workspace
   mkdir -p /root/project/pythonweb
   cd /root/project/pythonweb
   ```
![project-pythonweb](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/project%20folder%20and%20file.png)

- Initialize a local Git repository:
   ```bash
    git init
   ```
- Add the GitHub repository as the remote origin:
   ```bash
    git remote add origin <your repo url>

    # example:- git remote add origin git@github.com:anilrajrimal1/mypython.git
   ```
- Pull the existing master branch from the GitHub repository:
   ```bash
    git pull origin master
   ```
- List the files in the project folder:
   ```bash
    ls
   ```
- Open the index.wsgi file in a text editor and add python code:
   ```bash
    vi index.wsgi

    # add your python code
   ```

- Add and commit changes:
   ```bash
    git add -A

    git commit -m "mypython first commit"
   ```
- Push changes to the GitHub repository:
   ```bash
    git push origin master
   ```

![git-jobs-python](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/git%20work%20on%20Developer.png)

These commands create a new GitHub repository, set up a local Git repository, and push your Python project to the GitHub repository.
## 3. Creating a Job in Jenkins to Pull index.wsgi from the GitHub Repo and Send it to the Web Server in //var//www//html Directory


To create a Jenkins job for automating the process of pulling `index.php` from a GitHub repo and sending it to the webserver, follow the steps below:

### Open the Jenkins dashboard.

### Click on "New Item" to create a new job.

### Choose "Freestyle project" and provide a name for the job.

![project-Freestyle](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/create%20new%20job.png)

### Configure the Git repository details:
   - Under "Source Code Management," select "Git."
   - Enter the repository URL and provide the necessary credentials.

![project-git-add](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/add%20repo%20to%20job.png)

### Configure the Build Trigger:
   - Under "Build Triggers," select "Poll SCM."
   - Set the schedule to run the job using Cron syntax, e.g., `* * * * *` for polling every minute.

![build-Trigger](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/poll%20scm.png)

### Configure the Post-Build Action:

![post-build](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/post%20build%20action.png)

   - Under "Post-build Actions," select "Send build artifact over ssh."
     - Choose the SSH server previously configured (Anil-User).
     - Set the "Source files" to **/*	(or index.wsgi).
     - Set the "Remote directory" to `//var//www//html`.

  

   ```markdown
   - Jenkins Dashboard
     --> New Item (New Job)
       - Project name: <Your Job Name>
       - Type: Freestyle project
       - Source Code Management
         - Git
           - Repository URL: <Your GitHub Repo URL>
           - Credentials: <Select appropriate credentials>
       - Build Triggers
         - Poll SCM
           - Schedule: * * * * * (for polling every minute)
       - Post-build Actions
         - Send build artifact over SSH
           - SSH Server: Anil-User (Select server name)
           - Source files: index.wsgi or **/*
           - Remote directory: //var//www//html

```
- Click "Save" to create the Jenkins job.

Now, Jenkins is configured to pull index.html from the GitHub repo and send it to the webserver's //var//www//html directory after each build.

#### Console Output
![console-output](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/console%20output.png)


#### Webserver Result
![result](https://github.com/anilrajrimal1/mypython/blob/master/screenshots/on%20Anil-User.png)

