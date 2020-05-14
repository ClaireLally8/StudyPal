# Study Pal - Your Personalised Study Tracker 

Study Pal is a fullstack application targeting students studying in a class based or online set-up.  
The Study-Pal application was created to assist students in the organisation of subjects and notes, so each student can keep track of their subjects and topics within these subjects. 
The target audience, being studets, are able to create subjects and topics within one page and track their study by ticking off each subject as they complete. In another page, students are able to create, update and delete notes. 

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Colour Scheme**](#colour-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Known Issues**](#known-issues)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)
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

### Design
The overall design idea behind this was to keep the application as accessible for all users.

Keeping in mind current situation around the world, this application is aimed at students and instructors.  Where instructors can review a students progress within their courseload, and students can track their own progress, store and review notes also. 

### Framework

[Bootstrap](https://getbootstrap.com/)
- Bootstrap useage largely focuses on the responsiveness aspect of the appliaction

[Materialize](https://materializecss.com/)
- Materialize used for the general forms due to the clean and simple appearence. 

[JQuery v3.5.1](https://jquery.com/)
- In an bid to keep the JavaScript usage minimal, I chose to use jQuery as foundation to my scripts framework.
- JQuery(AJAX) was also used to prevent reloading of the page when a topic was marked off as complete. 

[Flask](https://flask.palletsprojects.com/en/1.1.x/)
- Flask is a microframework that I've used to render the back-end Python with the front-end.

### Colour Scheme

The Study-Pal application makes use of five core colours.
The primary colour being both #25443 and #FBFCBF

<img src="/static/imgs/colourscheme.png">

### Icons

- [Materialize Icons](https://materializecss.com/icons.html)
    - I replaced a lot of text areas with icons, specifically for the create, edit and delete functionality.  Each of these aspects makes use of the materialize icons, creating a smooth overall experience for the users. 
- [Font Awesome 5.8.1](https://fontawesome.com/)
    - Although Materialize Icons have nearly 1,000 free-to-use icons, I also made use of fontawesome icons on some aspects for the site. 
    The reason for this was solely due to creating a more beneficial User Experience. 
### Typography

Study-Pal uses two main fonts

    - Montserrat
    - Roboto
Both fonts were chosen for the sleek look and the ease as which they can be read by all visitors to the site. 


