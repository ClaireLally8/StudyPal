# [Study Pal - Your Personalised Study Tracker](https://study-pal.herokuapp.com/)
---
<div>
<img src ="static/imgs/Logo.png" alt="Logo" height="200" width="300" style="display: block;
  margin-left: auto; margin-right: auto;">
</div><br><br><br><br><br>
Study Pal is a fullstack application targeting students studying in a class based or online set-up.  
The Study-Pal application was created to assist students in the organisation of subjects and notes, so each student can keep track of their subjects and topics within these subjects. 
The target audience, being studets, are able to create subjects and topics within one page and track their study by ticking off each subject as they complete. In another page, students are able to create, update and delete notes. 
<br>
<br>
<br><br>

## Table of Contents
1. [**UX**](#user-experience)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Colour Scheme**](#colour-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

4. [**Information Architecture**](#information-architecture)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)
    - [**Database Schema**](#database-schema)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
<br>
<br>
<br>
 ## **User Experience**
---

### **User stories**
- As a vistior to the site I want to have a clear idea of the applications purpose upon visiting the site.
- As a student I would like to be able to create my own account
- As a student I want to view my personalised modules/notes on a daily/weekly basis
- As a student, I want to be able to create notes based on any subject I have on my courseload.
- As a student, I want to be able to track what topics I have studied and am yet to complete.
- As a student I want to be able to remove topics and subjects at the end of studies so i can start over again.
- As a student, I want to be able to edit and delete notes as I work through these also.
- As a student I want to be able to mark off what lessons I’ve completed as I progress on the courseload

- As an instructor, I would like to be able to view a students account using their @edu email address to view their study progress.

### **Design**
The overall design idea behind this was to keep the application as accessible for all users.

Features on the homepage was adapted from [inVision](https://www.invisionapp.com/) webpage with the content changed to suit the Study-Pal functionality. 

Keeping in mind current situation around the world, this application is aimed at students and instructors.  Where instructors can review a students progress within their courseload, and students can track their own progress, store and review notes also. 

The Study-Pal application is split into two parts. 
1) Home/Login/Register
- These sections consist of a navbr, main action section and a footer. 
    - Navbar - a responsive navbar with links to the `Home`, `Login` and `Register` pages.  
    - Main Action Section - this is where the information for the user lies, be it the information of the site itself, how the user logs in or registers an account.
    - Footer - A responsive footer, pinned to the bottom of the page, with Contact Details, links for the login, register & home page also. 

2) Subjects  & Notes pages.
- These pages consist of two sections.
    - Sidenavbar - both appealing to view.  On smaller screens, the navbar is a fullscren function and is triggers by a burger menu on the right corner of the page. 
    - Accordion that stores topics in the subjects pages or notes in the notes page.  After testing with a card functionality for these areas, there was greater postive feedback on an accordion feature for these sections. 

### **Frameworks**

[Bootstrap](https://getbootstrap.com/)
- Bootstrap useage largely focuses on the responsiveness aspect of the appliaction

[Materialize](https://materializecss.com/)
- Materialize used for the general forms due to the clean and simple appearence. 

[JQuery v3.5.1](https://jquery.com/)
- In an bid to keep the JavaScript usage minimal, I chose to use jQuery as foundation to my scripts framework.
- JQuery(AJAX) was also used to prevent reloading of the page when a topic was marked off as complete. 

[Flask](https://flask.palletsprojects.com/en/1.1.x/)
- Flask is a microframework that I've used to render the back-end Python with the front-end.

### **Colour Scheme**

The Study-Pal application makes use of five core colours.
The primary colour being both #25443 and #FBFCBF

<img src="/static/imgs/colourscheme.png">

### **Icons**

- [Materialize Icons](https://materializecss.com/icons.html)
    - I replaced a lot of text areas with icons, specifically for the create, edit and delete functionality.  Each of these aspects makes use of the materialize icons, creating a smooth overall experience for the users. 
- [Font Awesome 5.8.1](https://fontawesome.com/)
    - Although Materialize Icons have nearly 1,000 free-to-use icons, I also made use of fontawesome icons on some aspects for the site. 
    The reason for this was solely due to creating a more beneficial User Experience. 

### **Typography**

Study-Pal uses three core fonts

- `Montserrat`

    `Montserrat` is the primary font in the site.  Used on all the navigation links.  To make the content of the site more visually appealing and to highlight the hierarchy in the pages, I used four different weights of the font.   `500, 300, 200, 100.`

- `Karla`
    
    `Karla` was uesd for the header on the landing page.   As a slighly heavier weighted font than the other two fonts used, it draws the eye in to the main title of the application and emphasises this. 

- `Roboto`

    Roboto font was used variously throughout the site, used in the regular (300) weighting.  Roboto was chosen for the areas of the application that would have a lower level of importance than those using `Montserrat` and `Karla`.


### **Wireframes**

During the planning stages of the project, wireframes were created for desktop, tablet and mobile viewports.

- Desktop
    - [Landing Page](wireframes/Desktop/Landing-Page.png)
    - [Register](wireframes/Desktop/register.png)
    - [Login](wireframes/Desktop/login.png)
    - [Subjects](wireframes/Desktop/subjects.png)
    - [Notes](wireframes/Desktop/notes.png)
- Tablet
    - [Landing Page](wireframes/Tablet/Landing-Page.png)
    - [Register](wireframes/Tablet/Register.png)
    - [Login](wireframes/Tablet/Login.png)
    - [Subjects](wireframes/Tablet/Subjects.png)
    - [Notes](wireframes/Tablet/Notes.png)
- Mobile
    - [Landing Page](wireframes/Mobile/Landing-Page.png)
    - [Register](wireframes/Mobile/Register.png)
    - [Login](wireframes/Mobile/Login.png)
    - [Subjects](wireframes/Mobile/Subjects.png)
    - [Notes](wireframes/Mobile/Notes.png)

---
### Information Architecture
---


In order to sucessfully depict a users journey through the application, I created a Customer Journey Map.  Documenting each aspect of the applications CRUD functionality, from start to finish.

[**Customer Journey Map**](wireframes/charts/CustJourneyMap.png)

<br>
---
## **Features**

---
### Existing Features

### Features on multiple Pages


 - #### Navbar:
    - Study-Pal utilises two separate navbars, python checks if a user is logged in or not by using the `if email in Session` code and passes it to Jinja to determine which navbar to display.
        - If not in Session - the homepage, register page and login page will be displayed.  With a responsive navbar that contains links to the Home, Register and Login pages.
        - If in Session - the Subjects & Notes page is displayed.  A responsive side navbar that contains links to the two pages and a logout feature is displayed.
            - On Mobile, this page is hidden behind a burger menu, and when clicked is displayed on the full mobile page. 

- #### Footer 
    - A footer is displayed on the Home, Register & Login pages.  
        - The footer contains two main link areas.  1) (fictional) Contact Details for Study-Pal creators. 2) Navigation links to jump to the top of the page, redirec to the login or register pages.

---

### Features on individual pages   

#### Home Page

- Hero Image
    - The hero image is of a laptop, to signify the digital transformation of everything.  Accompanied by text on the left hand side, which is a brief low-down on the application and what it does.

- How it Works Section
    - Adapted from inVision's webpage - it utilises both text and icons to display the reasons for using the application and a brief description on how it works. 

#### Register & Login Pages
- These pages both follow the same structure: 
    - Main Image to the left of the page.
    - Form with email input & submit button on the right.

From testing, it was concluded that users eyes were drawn to the right hand side portion of the page, so the decision was made to put the form on the right hand side. 
There is also a link on the page to the opposed page (Register page contains a login link & vice versa)

#### Subjects Page

In the centre of the page, an accordion is displayed. 
- Upon loading, the accordion is closed & the subject name is displayed.
    - When clicked, the accordion opens and the topics are visible, where users can check off what they have completed, add and delete topics.  The process for adding a topic is similar to adding a subject. 

- A button on the bottom right of the page, when clicked, a modal for creating a new subject appears.  
This modal requests for users to input their subject name and add this subject.

#### Notes Page
Similar to the Subjects page, an accordion is found in the centre.

 - Notes are stored in this accordion.  A user clicks on the accordion and it expands.  Within this, there's an edit & delete button. 
 - Clicking the edit button, will relocate to another page where the user can update the note by changing the name and the notes content.
 - Clicking the delete button will reload the page and the note will be removed from the database it's stored in. 

<br>

## Features left to implement

There were several features planned for the future implentation of this project.

(1) Pagination
 - This was attempted several times throughout the creation of the project, however upon reviewing it was outside of my overall ability and the general scope of the application.

(2) Date Tracking
- This is a feature, again in the next implemetnation of the project aht I will be adding, where a user is able to record the date they would like to study the toic & the date they completed the topic also. 

(3) Classrooms 
- Where a user can join a virtual 'classroom' that they can join alongside their classmates.  Share notes and assist each other in the study process. 

(4) Progress Tracking 
- Where a student can compare where they are against other students in their classroom and review whether they are on track, ahead or behind the average of the classroom.

(5) Sharing notes with other users
- Upon entering a students email address, students are able to view others public notes and add them to their own notes section.  This feature will also involve the creation of private & public notes where users can share their notes with others, or choose not to share notes. 

(6) Ability to predict a pace
- When a user enters a start & end date for their study-pal, a user can then track their pace and what days they should be completing topcis and how many days they should be spending on each topic. 

---
## Technologies Used 
---
- Gitpod - Used as the IDE for this application.
- Github used for the remote storage of the code online.
- inVision Studio - used for creating the wireframes of the project.
- Adobe Illustator - Used to edit the images to meet the colour scheme of the application.

#### Font-End Technologies

- HTML - Used to create the structure of the application. 
- CSS - Used as the base for styling. 
- Javascript - Used to create interactivity within the project. 
- JQuery - Used for some of the main javascript functionality.
- AJAX - Used to prevent the page reloading upon writing to the database.
- Materialize - Used in conjunction with Bootstrap as the design framework. 
- Bootstrap - Used in conjunction with Bootstrap as the design framework. 

#### Back-End Technologies

- Flask - Used as the microframework.
- Jinja - Used for templating with Flask.
- Heroku - Used to host the application
- Python - The back-end programming language.
- Pymongo - Used to connect the python with the database.
- MongoDB Atlas - Used to store the database. 

#### Database Schema

- The application uses `MongoDB` for data storage.  MongoDB was chosen as the database to use due to the unstructured format of the data that will be stored within it. 

The data stored in the database are the following:
- Object ID
- String
- Boolean

There are four core collections within the Database: 

**Users**

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Email Address | email | email | string

**Subjects**

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Email Address | email | email | string
Subject | subject | text | string

**Topics**

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Email Address | email | email | string
Subject | subject | dropdown menu | string
Topic | topic | text | string
Complete| complete | checkbox | boolean (default to false)

**Notes**

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Email Address | email | email | string
Subject | subject | dropdown menu | string
Notes | note | text | string

The `email address` is added to each of the collections in order link all the the collections together. 

---
### Testing
---
All information on testing can be found in [Testing.md](testing.md)

---
## Deployment
---
### Local Deployment

**To run this project locally**

In order to run this project locally, you will need to install the following: 
- An IDE, such as [VS Code](https://code.visualstudio.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) to install the app requirements.
- [Python3](https://www.python.org/downloads/) to run the application
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for version control
- [MongoDB](https://www.mongodb.com/) to develop the database.


Once this is done, you will need need to download the .ZIP file of the repository, unzip this file and then in the CLI with GIT installed, enter the following command: 
   
    https://github.com/ClaireLally8/StudyPal.git

- Navigate to the to path using the `cd` command. 
- Create a `.env` file with your credentials. Be sure to include your `MONGO_URI` and `SECRET_KEY` values.
- Install all requirements from the requirements.txt file using the following command:
    
        sudo -H pip3 -r requirements.txt
- Sign up for a free account on MongoDB and create a new Database called StudyPlanner. The names of the databases collections can be found in the [database schema](#database-schema) section. 
- You should then be able to launch your app using the following command in your terminal:

        python app.py

### Remote Deployment

- Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.
- Create a Procfile with the terminal command `echo web: python app.py > Procfile`.
- `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.
- Head over to [Heroku](https://dashboard.heroku.com/login)
- Click the "new" button, give the project a name & set the region to Europe. 
- From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
- Confirm the linking of the heroku app to the correct GitHub repository.
- In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
- Set the following config vars:

| KEY | VALUE | 
--- | --- | --- | --- 
DEBUG| FALSE | 
IP | 0.0.0.0|
PORT | 5000|
MONGODBNAME | <database_name>
MONGO_URI| mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority 
SECRET KEY | <secret_key>

- In the heroku dashboard, click "Deploy".
- Your application should now be deployed.

### Content

All content for the Study-Pal application was written by me. 
---

#### Media

- Images were sources from [unDraw](https://undraw.co/), a site containing open soruce illustrations.
- Layout from the home-page was adapted from [inVision](https://www.invisionapp.com/)

#### Code

- I followed [this tutorial](https://www.youtube.com/watch?v=vVx1737auSE) on how to create the login functionality using Flask & Pymongo. 
- Code for the accordion was adapted from [WebDevTrick](https://webdevtrick.com/html-css-javascript-accordion-source-code/) & is credited in the JS code also.
- The Sidenav bar was adapted from two videos - [Animated Side Nav](https://www.youtube.com/watch?v=acuYmzY6XOg) and another youtube video which has since been deleted. 
