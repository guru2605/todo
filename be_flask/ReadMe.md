# Steps to Run Backend
> Todo Backend Application

# Setup Backend
``` bash
#Create A Virtual Environment
python3 -m venv env

#Activate Virtual Environment
source env/bin/activate


#Install All the packages from requirements.txt
pip install -r requirements.txt

#Export Environment Variables
FLASK_APP=app, FLASK_ENV=development

#Run Flask
flask run

#Database Used:
MongoDB (pymongo)
```