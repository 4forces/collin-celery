# SEIS - TEST #
By: Collin Wu Yuewei

### Installation ###
You can either download from the Github and unzip, then run the folder with your choice of editor.
```
https://github.com/CollinWuY/CeleryFiles
```
__OR__

Clone the repo using
```
git clone https://github.com/CollinWuY/CeleryFiles
```

### Project Scenario ###
To create 3 Components:
1) REST API web Service
- Upload File (txt)
- List Files
    - Information
    - File Size
    - File Name /w path
1) Celery /w Celery Beat
- Periodically scan files, read, and calculate the sensitivty scores base on list given
- Update the sensitivity scores to the DB with updated timestap
3) Single Page React Application
- Upload File functionality
- List information of files that are uploaded

### Frameworks Used ###
- Django
- Django-REST-framework
- React.js
- Postgresql
- Celery
- Celery Beat
- Docker

### How to Use/Test ###
- Run the directry in your editor / clone the git repo into editior
- Open terminal, ensure file path is in the Django application Project folder with the manage.py 
```
./CeleryFiles/CeleryApp/
```
- Use docker compose to launch the application
```
docker-compose up
```
- Open browser to http://127.0.0.1:8000

### Endpoints ###
```
/
/api
    /api-list/
    /api-details/<str:pk>/
    /api-create/
    /api-delete/<str:pk>/
/admin
/accounts
    /login/
    /logout/
    /signup/
/sensitivefiles
    /files/<user_id>/
```
## Note: There are two verisons of the scenario: 1) React.js + DjangoRestFramework ||  2) Django + AllAuth ##

### React UI + Django-REST-Framework ###
The main page is created based on the scenario given. It consist and UI page by React.js with an upload field, a submit button and a button to show all files uploaded with information required. The delete button deletes the files from the React database.
#### Testing React/REST version ####
- Upload a file, ONLY accepts .txt
- Submit
- Click the View Uploaded Files to see uploaded files
##### Things not Implemented Yet #####
- An authentication system to check user and log user uploading
- Limit the user to only being able to delete user's upload
- A manual sensitivity checker and updater button
###### Reasoning for Implementation ######
- React has been split into components to for easier deployment and repeated deployment of each component on the main App.js
- Security and user tracking is needed to prevent other users from deleting records that are not theirs for traceability, therefore I think it should be implemented; as shown in the Django+Allauth scenario


### Django + Allauth ###
The scenario was built originally to bring forth what was needed by the scenario. **Not required**
Build using Django and Allauth, with base.templates and template inheritance.
As this is not part of the scenario, there is no direct button to this part of the site.
- To access: In browser go to the sensitivityfiles endpoint
```
http://127.0.0.1:8000/sensitivefiles/
```
#### Testing Django/Allauth version ####
- In order to use the upload, you are required to login
```
Sample Accounts
| Permission | User Login | Password |
| ---------- | ---------- | -------- |
| superuser  | admin      | admin123 |
| normal     | test       | tester123 |
```
- You can create your own account by clicking **Register** on the Navbar
  - An email will be create in the Terminal Console, click on the link to activate the email
  - Login with username and password **not email**

- Functions exactly like the front React/REST scenario but has restrictions of user login and user id access to the files uploaded
- **Checker** button is avaible to manually run the sensitivity checker

### Sensitivity Checking and Updating ###
- The process is automated with Celery + Celery beats, which runs a task to rrun a function that reads and update all files in the current database **EVERY 5 MINUTES**
- Docker will be running the task management on launch with the RabbitMQ broker
- ONLY in the Django/Allauth there is a button to call **Checker** manually