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
