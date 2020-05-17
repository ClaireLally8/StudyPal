This is an extension from the [README.MD](README.md) file.

You can view the deployed application [here](http://study-pal.herokuapp.com/base)

---
## Table of Contents

1. [**Code Testing**](#code-testing)
    - [**Validator Testing**](#validator-testing)

2. [**User Experience Testing**](#ux-testing)

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