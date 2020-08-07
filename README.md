# README - Superhero Name Generator

QA SFIA2 Project

## Table of Contents

**Project Brief**

**Planning**

**Risk Assessment**

**Project Architecture**

**Final Application**

**Deployment**

**Retrospective**

## Project Brief

The main goal of this project was to utilise a number of different technologies to deploy an application that met certain key requirements. These Key Requirements were:

+ Using Python to Develop 4 Micro-Services with a RESTful architecture
+ Services 2, 3 and 4 should have dual implementations
+ The result of Service 4 should be stored in a MySQL Database
+ Docker should be used to containerise the 4 Micro-Services
+ Docker Swarm must be used to deploy the containers over a minimum of 2 nodes
+ Ansible must be used to configure the environment of the Nodes prior to the application being deployed
+ A CI/CD Pipeline using Jenkins will automate the entire process of Build/Test/Deploy

### Proposal

My proposal was to create a Superhero Name Generator. My inital proposal includes 4 services as follows:

+ Service 1: This will be the front end of my application, and Flask will be used to create this. My database will store the resulting Superhero Name that is generated from Service 4 in a MySQL Database on GCP. Only a single index.html page will be used to display the information.

+ Service 2: Generates a random First Name to return to Service 4.

+ Service 3: Generates a random Second Name to return to Service 4.

+ Service 4: Returns to Service 1 a Superhero Name based off of the First Name and Second Name returned from Service 2 and 3. All Data is formatted and returned to Service 1.

![An Initial Wireframe diagram of my Flask Application (Service 1)](https://i.imgur.com/fkj4ND1.png)

Shown above is an initial Wireframe diagram of my Flask Application (Service 1)

## Planning

### Initial Trello Board

Trello, a web-based Kanban board, was used to plan the project while implementing AGILE methodology, such as specifying a product and sprint backlog. The project was to be split into 2 sprints. I utilised MosCoW Prioritisation to give each requirement of the project an importance, so that I can use this to sort the order I should prioritise completing them in. I used a colour labelling method to do this and you can see an example of this below for my Initial Trello Board:

![Initial Trello Board ](https://i.imgur.com/WXKOUzu.png) 

![Labels](https://i.imgur.com/8yfZvZX.png)

### Sprint 1 

The main aims in Sprint 1 were to create the 4 micro services and ensure they work together, as well as gain experience using Docker, Docker Swarm and Docker Swarm as early as possible so that the micro-services can be containerised. This is reflected in the Initial Sprint 1 board below:

![Initial Sprint 1 ](https://i.imgur.com/4OBGydL.png)

#### Rolling Changes During Sprint 1

+ Service 1 Constructed using Flask
+ Service 2 and 3 Randomly Generates Names
+ Service 4 returns data back to Service 1
+ Dockerfiles created for each service to enable Containerisation
+ First Version of Application containerised using Docker and pushed to repo on Docker Hub
+ First Version of Application run using Docker Compose with updated Docker-Compose file
+ First version of Application runs on multiple VM's using Docker Swarm
+ Database Successfully integrated
+ Latest Version of Application runs on multiple VM's using Docker Swarm
+ Exposed TCP/UDP Ports required for Docker Swarm, on GCP VM Instance Firewalls
+ All Docker images version controlled using Docker Hub
+ All work files version controlled using GitHub

### Sprint 1 (end) / Sprint 2 (start)

All changes during Sprint 1 were explained above. The main aims in Sprint 2 were to create a Ansible Playbook to configure the VM's that would be used in the Swarm, build a Jenkins Pipeline to Build the compose file and deploy the application to multiple seperate VM's. Shown Below is the Trello Board by the Start of Sprint 2:

![End Sprint 1 ](https://i.imgur.com/6nUR5AU.png)

#### Rolling Changes During Sprint 2

+ Nginx implemented as a container for Reverse Proxy
+ Ansible Playbook written to install Docker on target VM's using inventory file
+ Ansible Playbook updated to also create Manager/Worker Nodes using inventory file
+ Ansible Playbook updated to also deploy Docker Swarm Stack Application
+ Jenkins Pipeline established on seperate VM with webhooks from Master branch of Github Repo
+ Jenkinsfile written as well as accompanying sh scripts
+ Jenkins CI/CD Pipeline Build stages successful
+ App Relevant Secret Info + Ansible Files stored on Jenkins Server
+ Ansible File update to also copy files during deploy stage, to multiple VM's and deploy the Swarm Stack Application
+ Jenkins CI/CD Pipeline successfully built
+ All work files version controlled using GitHub
+ Webhooks created for Dockerhub Images

### Sprint 2 (end)

All changes during Sprint 2 were explained above. The Trello board by the end of the Final Sprint is shown below:

![End Sprint 2 ](https://i.imgur.com/9tWrVBI.png)

By the end of Sprint 2 the key requirements as well as some optional requirements were implemented. However All 'Could Have' labelled features were not implemented due to time constraints, however these would be considered in a future sprint. This will be discussed later in the README.

#### Issues Faced During The 2 Sprints:

+ Had issues with setting up Docker Swarm as Worker Nodes could not pull down image. Fixed by Making Docker Repo Public
+ Had issue where exposing API key as well as DB info needed to be prevented. An Environment File was made and used to store the environment variables so that it can be used on multiple VM's
+ SSH keys are needed to be used for Ansible to execute all instruction in Playbook on other VM's. SSH keys were securely transferred to relevant folders
+ Multiple minor issues with Docker Swarm, however these were fixed by checking the logs of the service or container and identifying potential causes e.g. missing dependecy, Database not on etc

## Risk Assessment

### Initial Risk Assessment and Matrix

Shown below is the intial risk assessment and accompanying matrix for the project:

![Initial RA](https://i.imgur.com/4SQ40yl.png)

![Initial Matrix](https://i.imgur.com/rpZr832.png)

### Final Updates to Risk Assessment and Matrix

Shown below are additions to the risk assessment and matrix after completing the project and encountering a further number of issues:

![Final RA](https://i.imgur.com/euVDQuN.png)

![Final Matrix](https://i.imgur.com/HdFVCrf.png)

## Project Architecture

### Entity Relationships

The initial ERD Diagram for my project is shown below. The database consists of a single table called currencylist, in which the pair and price returned to Service 1 is stored.

![Initial ERD](https://i.imgur.com/YVzpN5s.png)

#### Docker Swarm / UI Architecture

Shown Below is the Docker Swarm architecture for the application. The Swarm Architecture consists of 2 GCP VM Instances, in which one VM instance is configured to be a Manager Node, and the other a Worker Node. An Overlay network is used to deploy the swarm so that the applications can communicate with each other from different VM's. There are a total of 5 Docker Containers used. 4 Containers are for the actual developed service, while the 5th container is an Nginx Image, which is acting as a Reverse Proxy to forward port 80 web traffic to port 5000 of the Flask App and vice versa. Services 1, 2, 3 and 4 are replicated 3 times, while Nginx is only Replicated once.

![Docker Swarm Architecture Diagram](https://i.imgur.com/yehYnpZ.png)

#### Deployment Pipeline

The Pipeline used for deployment is shown in the diagram below. The Entire Pipeline utilises 2 GCP VM instances. 1 is used for developing the application as well as being the Master node in the swarm and the Jenkins Server, and another VM instance is utilised as a worker node. All VM instances have access to the GCP SQL Database so that the flask application can retrieve and store data wherever the container may be.

![Deployment Pipeline](https://i.imgur.com/txZfyIl.png)

#### Toolchain 

The Toolchain Pipeline is shown below: 

![Toolchain Pipeline](https://i.imgur.com/tOm78eo.png)

## Final Application

The Final design of the website is shown below.

![Screenshot of Final Webapp](https://i.imgur.com/oTJHTEE.png)

## Deployment

### Technology Used

+ 2 GCP VM Instances
+ 1 GCP SQL Server for storing Data
+ Jenkins Pipeline for CI/CD with Github Webhooks
+ Ansible to configure the environment of deployment VM's
+ Docker to Containerise the application
+ Docker Swarm and Docker Compose to run the Application across multiple VM's
+ NGINX as a reverse proxy
+ Docker Hub as a Version Control Service for Docker Images
+ GitHub as a Version Control Service for the Applications Code

## Retrospective

### What Went Well

+ Project completed within timeframe
+ All 'Must Have' Requirements Met
+ Docker, Ansible and Jenkins all Successfully Integrated into a continuous pipeline
+ Application deployed across multiple VM's

### Future Improvements:

+ Improve page layout and design
+ Deploy application to more worker nodes
+ Incorporate a second manager node in Swarm to ensure system reliability

## Author

Scott Halliday

