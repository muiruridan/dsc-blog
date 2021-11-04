# GDSC JKUAT WEB APP

This project comprises the backend and frontend powering the GDSC JKUAT web application.
## Tech

Backend is written in Django 3.2 (Python) while frontend in HTML, CSS and JS

Frontend will soon be moved to ReactJS or React with Typescript.

## Setup

* If you had already cloned/downloaded the repository, then pull the current changes using:
```shell
git pull https://github.com/jkuatdsc/dsc-blog.git
```
Lest....

* First, clone the repository:

```sh
git clone https://github.com/jkuatdsc/dsc-blog.git
cd dsc-blog
```

* Create a virtual environment to install dependencies in and activate it:


```sh
python -m venv <envname>
source <envname>/bin/activate 
```
or for Windows using Git Bash,
```shell
python -m venv <envname>
./<envname>/Scripts/activate
```

* Install requirements in the virtual environment created:

```sh
pip install -r requirements.txt
```



* Run database migrations with this command

```sh
python3 manage.py migrate
```

* Run server to ensure everything is working properly.

```sh
python3 manage.py runserver
```

### Collaboration
Clone the repository and please read the [contributing guide](/CONTRIBUTING.md).

### License
This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for more details.
