# Hello Web App Tutorial
https://hellowebapp.com/tutorial/

## Sasebo Code Club Project
We purchased the book and began working on this tutorial in April (2017) as an introduction to Django and Python.

### Notes

#### Virtual Environment
A virtual environment allows your projects to use separate versions of Django and other plugins. This means changes made to one project won't affect any others you may be developing.

Within the project folder, type `virtualenv venv` on the command line to create the virtual environment, like so:
`projects/myhellowebapp $ virtualenv venv`

Then you must activate it with:
`source venv/bin/activate`

Finally, you can run the python server:
`python manage.py runserver`

#### Chapter 4: Setting Up Your Templates
Before starting Chapter 4, take a few minutes to:
- [ ] read https://github.com/hellowebapp/hellowebapp/tree/master/git-tips and set up your .gitignore file
- [ ] create a README.md file in the top level directory
- [ ] set up a GitHub repository

#### Chapter 9: Forms.py Funsies
According to [DiveIntoPython](http://www.diveintopython.net/getting_to_know_python/indenting_code.html), "code blocks are defined by their indentation." If you receive an error at the end of Chapter 9 stating "The view xxxxx didn't return an HttpResponse object. It returned None instead," check views.py to make sure the if statements defined for edit films are indented properly. You can view the branch for Chapter 9 at https://github.com/hellowebapp/HelloWebApp-Code/tree/chapter-9.

#### Chapter 11: "One Last Thing"
Chapter 11 ends with a challenge to figure out how to add the ability for logged in users to change or update their password using the password_change templates created in Chapter 10. Even though I knew the answer, I did not trust myself and spent too much time over-thinking it. Don't be like me. Create the urls, add the link, and move on.

#### Chapter 13: Quick Hits
After running `pip freeze`, I noticed `wsgiref==0.1.2` was not listed. According to [this post](http://discuss.hellowebapp.com/t/missing-wsgiref-0-1-2-when-i-pip-freeze/32), it is installed automatically with Python and is not needed in the requirements.txt file.

#### Chapter 14: Deploying Your Web App
If you already have apps on Heroku, you can skip ahead to "Installing a few extra packages." And, a word of caution, make sure you are in the myhellowebapp directory before running `heroku create`. 
