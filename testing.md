This is an extension from the [README.MD](README.md) file.

You can view the deployed application [here](http://study-pal.herokuapp.com/base)

---
## Table of Contents

1. [**Code Testing**](#code-testing)
    - [**Validator Testing**](#validator-testing)
    - [**Compatibility Testing**](#compatibility-testing)
    - [**Known Issues**](#known-issues)
        - [**Resolved**](#resolved)
        - [**Unresolved**](#unresolved)

2. [**Functional Testing**](#functional-testing)
    - [**User Testing**](#user-tests)
    - [**Manual Testing**](#manual-testing)

---
### Code Testing
---
#### Validator Testing

[W3C Markup Validation](https://validator.w3.org/)
 - W3C was used in the validation of both the HTML and CSS for the application.
    - Some minor errors were encountered with `<div>` tags being used within a `<button>` tag. This was repalced by a `<span>` tag.
    - Another determined was the repeated use of an id in the accordion content.  This was adjusted to a class tag and resolved. 
    - No errors in the CSS were noted. 

[JSHint](https://jshint.com/) was used to validate the Javascript.
- When run through the JSHint validator these metrics were returned :
    - There are 7 functions in this file.
    - Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 8 statements in it, while the median is 3.
    - The most complex function has a cyclomatic complexity value of 2 while the median is 1.
- Four warning were noted in the JSHint validator: 
    - Two of these warnings were missing semi-colons which have been resolved. 
    - const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    - 'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').
- Two undefinied variables were noted which are due to the use of JQuery: 
    - $
    - sidemenunav

[JSesprima](https://esprima.org/demo/validate.html)
- "Code is syntactically valid"

[Python PEP8](https://pypi.org/project/autopep8/)
- The autopep8 extension was installed in the workspace. 
    - To install this enter this in the terminal: 
        -   `pip3 install --upgrade autopep8`

    In order for autopep8 to run, [pycodestyle](https://github.com/PyCQA/pycodestyle) is also required. 
    To instlal pycodestyle, enter this command into the terminal: 
    -  `pip3 install pycodestyle`

- Once these steps are complete, you can format the code into PEP8 formatting by entering this command into the terminal:
    - `autopep8 --in-place --aggressive --aggressive app.py`

Due to my overall experience with Python, I elected not to follow the PEP8 formatting during the creation of the application, however decided to format the code into PEP8 after the `app.py` was written.  
Now after this application is complete, I am more aware of the requiremetns to follow t follow the PEP8 formatting and will be following this in the future.

When the `app.py` code is pasted into [PEP8 checker](http://pep8online.com/), three warnings are presented:
 
 1. line too long (88 > 79 characters)
 2. line too long (91 > 79 characters)
 3. line too long (90 > 79 characters)

 These errors flagged are down to the flask app routing for returning variables to display content in the HTML file and no way to resolve these has been discussed.

 #### Compatibility Testing
 To ensure a the maximum amount of users are able to use this application.   I tested it's compatibility among various browsers and device screen sizes :
 
 - Browsers
    - Chrome
    - Firefox
    - Safari
    - Opera
    - Microsoft Edge
- Screen Sizes
    - 21-inch display
    - 15-inch display
    - 13-inch display
    - 10-inch display
    - 6-inch display
    - 5-inch display    

#### Known Issues

##### Resolved 

- An issue with the footer not sticking to the bottom of the page was highlighed on the 10-inch display on all browers. This issue was resolved using code adapted from this [Medium Article](https://medium.com/@zerox/keep-that-damn-footer-at-the-bottom-c7a921cb9551)
- Completed Topics only checked off after the page reloaded 
    - This was resolved by creating a JS function which add/removes the classname isComplete upon clicking the checkbox, which changes the colour of the topic font.
    - This function also toggles the `checked` field to true/false
- Subject accordion displaying multiple times for each topic
    - To resolve: I had to alter the app route so the topics variable was returned in a list.  Then the for loops in the HTML were pulled in and looped thorugh so that each subject would display once, and the topics related to that subject will be found within the accordion.

##### Unresolved

There is one key bug that due to both time and skill restraints I found I am unable to resolve: 

- Upon manually entering the `http://study-pal.herokuapp.com/modules` or the `http://study-pal.herokuapp.com/notes`.  The page content is displayed without an email in the Session.
    - Attempts to resolve this using an if (email in Session) statement was made, however this issue was still presented for these pages.
- Select tag in HTML not defaulting to the subject name where the '+' icon is clicked.  Attempts were made to resolve, however due to lack of knowledge on why this was an issue, I was unable to resolve the issue. 
No other known bugs were presented upon review of the application.

---
### Functional Testing
---

Usability tests were conducted to ensure a positive User Experience and the site was functioning correctly and as intended : 


#### User Tests

A single usaibility test was undertaken to ensure the application was easy-to-use and accessible for all student ages and backgrounds.
- Test 1
    - A  student, studying for your university exams.  Create an account using the email address hello@test.com. 
    - Create two subjects relating to a module on your coursework, called "Calculus" and "Statistics" 
    - Make three topics, differentiation, integration under the calculus subject, and standard deviation under the statistics subject. 
    - Create a note, under the subject, Differentiation, called definition with the definition "In Calculus, derivative is the measure of how a function changes its value as the input changes"
    - Create another note, under Statistics, again, called definition,  with the note "In statistics, the standard deviation is a measure of the amount of variation or dispersion of a set of values." 
    - Edit the differentiation note, and change the name to "Introduction to derivatives" and add the line "the derivative of y (with respect to x) is written dy/dx"
    - Now, go to the topic and check off the topic, differentiation. 
    - Your lecturer has emailed, standard deviation is no longer on the exam, so you must delete everything from the application about standard deviation, note and topic. 
    - Logout of your account. 

**Feedback From User Test**
There was some feedback given from the user test.
- Altering the colour of some text to make it stand out more to the user
- Upon editing a note - the subject of that note disappears.  This error has been resolved. 

#### Manual Testing

In order to ensure the application functioned as required, I manually tested all aspects of the deployed site.

**Home Page**
- Checking links in navbar to home, login and register pages redirects.
    - Functioning correctly & as expected
- Checking links in footer, to ensure jump to top, login, register reidrect work. 
    - Functioning correctly & as expected

**Login Page**
- Check logging in with insufficent email address (no @ format, no . format)
    - Functioning correctly & as expected
- Check logging in with an address that isn't a registered email.
    - Functioning correctly & as expected - however adjusted flash message and re-direct path to enhance overall user experience. 
- Testing URL to redirect to registration page.
    - Functioning correctly & as expected

**Register Page**
- Check registering with insufficent email address (no @ format, no . format)
    - Functioning correctly & as expected
- Check registering with an already registered email address
    - Functioning correctly & as expected - however adjusted flash message and re-direct path to enhance overall user experience. 
- Testing URL to redirect to login page.
    - Functioning correctly & as expected

**Subjects Page**
- Check creating a subject button
    - Functioning as expected
- Check adding a subject with no subject name
    - Modal closing without flashing error on lack of subject name.  RESOLVED: Resolved by the removal of the `modal-close` classname in the HTML for the modals.
- Check creating a topic button
    - Functioning as expected
- Check creating a blank topic with no name
    - Functioning as expected
- Check creating a topic defaulting to subject where '+' was clicked
    - Not functioning - marked in known issue as unable to resolve.
- Check marking a topic as complete & unchecking complete
    - Functioning as expected
- Deleting a topic
    - Functioning as expected

**Notes Page**
- Check creating a note button
    - Functioning as expected
- Check adding a note with no note content
    - No error returned.  Issue resolved & updated. 
- Check adding a note with no subject
    - Functioning as expected
- Check adding a note with no title
    - Functioning as expected
- Check editing a note to make blank
    - No error returned.  Issue resolved & updated.
- Check deleting a note
    - Functioning as expected


**Logout**
- Check Logout functionality
    - Functioning as expected