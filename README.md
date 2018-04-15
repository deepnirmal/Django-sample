# To_Do_Application
##This is a sample ToDo app using Django and TasyPie

### Run the project 
`python3 manage.py migrate`
`python3 manage.py testserver`

### OR Buid using Docker image
Using Docker file
`docker build -t django-to_do_app .`
`docker run --name=Django -td django-to_do_app`

## Specs and feature

1. A task will have a `title` and `due-date`.

![main_app](images/Screen Shot 2018-04-16 at 12.52.31 AM.png)

2. There are only 2 state applicable for task. Pending or Completed 
Restricting the user from the UI 
![task_status](images/Screen Shot 2018-04-16 at 12.54.20 AM.png)

3. Ascending by due date
`http://localhost:8000/api/v1/task/`
![due_date_orderby](images/postman.png)



