<h1 align="center">🏨 Hotel Management</h1>

<br>
<p align="center">
<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"/> <br><br>
<a href="https://www.python.org/" target="blank"><img align="center" src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="python"/></a>
<a href="https://www.djangoproject.com/" target="blank"><img align="center" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="django" height="37" width="90"/></a>
</p>
 
## Project :

### About :
This is a Open Source Hotel Managment website. This project is made to serve a modern day Hotel to take it's Management online.
The project serves to both the internal and exterior functioning of the 🏩 Hotel such as Website, 🛏️ Explore rooms, 📒 book them and as well as ❌ cancel them if situation arises. <br>
💵 **Razorpay Payment Gateway** is also integrated in this website. <br><br>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/home.jpeg" alt="main"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/home2.jpeg" alt="main2"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/room.jpeg" alt="roomlist"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/explore.jpeg" alt="explore"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/explore2.jpeg" alt="explore2"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/bookings.jpeg" alt="bookings"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/cancel.jpeg" alt="cancel"/>

------------

### Project Setup :

Prerequisites
1. python3
2. pip3


3. Clone the project.

    ```shell
    git clone https://github.com/shashank725/Hotel_Management.git
    ```
    

4. Create a virtual environment with venv (install virtualenv, if its not installed) inside the project floder.
  
    ```shell
    cd Hotel_Management
    ```
  
   #### For Linux/Mac OSX
    ```shell
    sudo apt-get install python3-venv
    python3 -m venv env
    ```
  
   #### For Windows
    ```shell
    pip install virtualenv
    python -m venv env
    ```


5. Activate the virtual environemnt.

    #### For Linux/Mac OSX
    ```shell
    source env/bin/activate

    ```

    #### For Windows
    ```shell
    env\Scripts\activate

    ```
   
6. Install the requirements.

    ```shell
    pip install -r requirements.txt
    ```
 
7. Run the Migrations

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

8. Run the development server

    ```
    python manage.py runserver

    ```
9. Head to server http://127.0.0.1:8000

