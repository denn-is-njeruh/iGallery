## Project Name
**iGallery**


## AUTHOR 
**Dennis Njeru**


## DESCRIPTION 
This application depicts a personal gallery where the admin can post photos and users  get to view them. Users can expand the images by clicking on them, know the shooting location, copy and share a link to the image, and search for images.


## Features
As a user of the application you will be able to:
1. View different photos that interest you.
2. Click on a single photo to expand it and also view the details of the photo. The photo details will appear on a modal within the same route as the main page.
3. Search for different categories of photos. (ie. Movie, Sports, Nature)
4. Click on share icon to share the image with any of your social account or alternatively Copy a link to the photo and share with your friends.
5. View photos based on the location they were taken or category.


### Installation and setup instructions
1. Clone this repo: git clone https://github.com/denn-is-njeruh/iGallery.git
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://realpython.com/pipenv-guide/)
3. To run the app, you'll have to run the following commands in your terminal

        pip install -r requirements.txt
4. On your terminal,Create database gallery using the command below.

        CREATE DATABASE gallery;
5. Migrate the database using the command below

        python3.6 manage.py migrate
6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

        python manage.py runserver
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


## Running the tests
Use the command given below to run automated tests.

        python manage.py test gallery


## TECHNOLOGIES USED 
* Django
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface


## KNOWN BUGS
No known bugs at the moment.


## CONTACTS
* Email: dennis.njeru@student.moringaschool.com 
* LinkedIn: https://www.linkedin.com/in/dennis-gitonga-227246193/

## LIVE LINK



## LICENSE 
[GNU GPL v3.0](./LICENSE)


Copyright (c) [2021] **Dennis Njeru**