# **SFIA2 Project - Superhero Name Generator**

## **Resources**
- Trello - https://trello.com/b/KdnuhFZX/collectibles-week-5-project
- Website - http://35.214.55.107

### **Contents**
- Brief
  * Minimum Requirements
- Functionality
- Data
- Tech Stack
- CI Pipeline
- Front End Design
- Risk Assessment
- Difficulties
- Future Improvements
- Authors

### **Brief**
The brief for this project was "To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training".
This meant building an app that could take input from a user in order to create, read, update and delete data in a database while also making this visible to the user via the app itself.

#### **Minimum Requirements**
- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- This could also provide a record of any issues or risks that you faced creating your project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

### **Functionality**
To satisfy the brief I designed an app that would allow users to create a list of collectibles that they owned.
The users stories that satisfied the brief were:
- As a User, I would like to have a function that allows me to CREATE/ADD to the database.
- As a User, I would like to have a function that allows me to READ the database.
- As a User, I would like to have a function that allows me to UPDATE the database.
- As a User, I would like to have a function that allows me to DELETE from the database.

The below images show all the user stories created for this app as well as the layout and flow of the AGILE cycle that was implemented throughout.

![Image of Trello](https://i.imgur.com/4OlAZsg.png)

![Image of Trello2](https://i.imgur.com/Xb3JU74.png)


### **Data**
It is important to outline what data will be included in the database and how it will all relate. The entity relationship diagram (ERD) below shows this.

![Image of ERD](https://i.imgur.com/BpNspeC.png)

The ERD shows the relationship between the Collectibles and Users tables.

### **Tech Stack**
The below tech stack was implemented for this project.
- GCP SQL Server
- GCP Virtual Machine
- Trello
- Python
- Flask
- Git
- Jenkins

### **CI Pipeline**
The below image shows the flow of the app and how the tech stack is used in the Continuous Integration (CI) Pipeline.

![Image of CI Pipeline](https://i.imgur.com/XtTKaBB.png)

### **Front End Design**
The front end design of the app is very basic and is made to be functional as shown in the wireframe below.

![Image of Wireframe](https://i.imgur.com/MIkgumo.png)

The apps URL will take the user to the Home page.

![Image of Home](https://i.imgur.com/JdERLlp.png)

*About page.*

![Image of About](https://i.imgur.com/ISU68dN.png)

*New users need to register.*

![Image of Register](https://i.imgur.com/xFza8WI.png)

*Users can then use the login page.*

![Image of Login](https://i.imgur.com/pmWHMzA.png)

*Logged in users see their content on the home page.*

![Image of Logged In Home](https://i.imgur.com/nzK7ccy.png)

*Logged in users have access to My Account page.*

![Image of My Account](https://i.imgur.com/HCkVsii.png)

*Once logged in users can add collectibles to their list.*

![Image of Add Collectible](https://i.imgur.com/WQTxwkn.png)


### **Risk Assessment**

![Image of Risk Assessment](https://i.imgur.com/6fieRm3.png)

### **Difficulties**
The main difficulties encountered were ones of my own making, pieces of code missing or references not answered.
With my own incompetance aside other issues involved design. My initial designs for the appearance and operation of the app were far more difficult to employ than I anticipated. Things such as drop down menus and images were put aside and changed to allow easier functionality.

### **Future Improvements**
- To allow social media integration to allow the sharing of users lists
- To improve the pages design, include images and more colour

### **Author**
Scott Halliday
