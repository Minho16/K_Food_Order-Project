# K_Food_Order-Project


This is a web application that allows the users to search dishes by categories, add items into the cart by clicking the plus/minus buttons below each image.
The selected items will be displayed in the drawer and will be moved into Order list when the order button is clicked. 

(1) Main page with all items shown
![alt text](https://github.com/Minho16/K_Food_Order-Project/blob/main/image.jpg?raw=true)

(2) Main page when the cart-drawer is open
![alt text](https://github.com/Minho16/K_Food_Order-Project/blob/main/image2.jpg?raw=true)


**How to setup**

1. Select a folder where you want to clone the code

2. Clone the code https://github.com/Minho16/K_Food_Order-Project.git

  ```sh
  git clone https://github.com/Minho16/K_Food_Order-Project.git
  ```
  
3. Go to the directory where requirements.txt is located 

  ```sh
  cd (...)/"your folder"/K_Food_Order-Project
  ```

4. Set virtualenv in the same directory and activate it

```sh
  virtualenv env
  ```

```sh
  cd env/Scripts
  ```

```sh
  . activate
  ```

5. Go to the directory "your folder"/K_Food_Order-Project/k_food_order_django and run server

```sh
  python manage.py runserver
  ```

6. Open another terminal and go to "your folder"/K_Food_Order-Project/k_food_order_vue

7. install npm
 
 ```sh
  npm install 
  ```

8. run serve
 
 ```sh
  npm run serve
  ```

9. Now the app is already running at localhost (ex: http://localhost:8080/)



Below dependencies need to be installed:

  Backend: django
  - django
  - django-rest-framework
  - django-cors-headers
  - djoser
  - pillow 

  Frontend: vue.js
   - -g @vue/cli (vue 2.x // babel, router, vuex, CSS Pre-processors)
   - axios
   - vuetify

Need to be improved: 
 - Increase the ordered_number of the items that are ordered(purchased) by API 'POST'
 - Sign Up and Log In
 - Combine cart state & log-in 


