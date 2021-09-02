# Hotel_Management

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

An app where you can book rooms and view your bookings !

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/home.jpeg" alt="main";/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/home2.jpeg" alt="main2" style="width:200px;"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/room.jpeg" alt="roomlist" style="width:200px;"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/explore.jpeg" alt="explore" style="width:200px;"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/explore2.jpeg" alt="explore2" style="width:200px;"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/bookings.jpeg" alt="bookings" style="width:200px;"/>

<img src="https://github.com/shashank725/Hotel_Management/blob/main/system/static/system/cancel.jpeg" alt="cancel" style="width:200px;"/>

<h3>Starting the project</h3>

Prerequisites
1. python3
2. pip3

3. Create a new directory.

  ```shell
  mkdir Hotel_Management
  cd Hotel_Management
  ```

4. Create a virtual environment with venv (install virtualenv, if its not installed).

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

5. Clone the project.

    ```shell
    git clone https://github.com/shashank725/Hotel_Management.git
    ```

6. Activate the virtual environemnt.

    #### For Linux/Mac OSX
    ```shell
    source env/bin/activate

    ```

    #### For Windows
    ```shell
    env\Scripts\activate

    ```
   
7. Install the requirements.

    ```shell
    cd Hotel_Management
    pip install -r requirements.txt
    ```
 
8. Run the Migrations

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

9. Run the development server

    ```
    python manage.py runserver

    ```
10. Head to server http://127.0.0.1:8000



