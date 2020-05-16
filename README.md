# Study Pal - Your Personalised Study Tracker 

Study Pal is a fullstack application targeting students studying in a class based or online set-up.  
The Study-Pal application was created to assist students in the organisation of subjects and notes, so each student can keep track of their subjects and topics within these subjects. 
The target audience, being studets, are able to create subjects and topics within one page and track their study by ticking off each subject as they complete. In another page, students are able to create, update and delete notes. 

## Table of Contents
1. [**UX**](#user-experience)
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
    
### **Framework**

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


