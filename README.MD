SaveASpecies
 Django/Python Website that gives users credible organization sources that they can donate to save a species they feel passionate about.

** Use Case: Allows animal donors and animal activist to connect with multiple foundations/organizations on a platform that sets a aunthentic, and quality foundation. **

How The Program Works:
You are on the landing page that has an intro video about what the website is about along with background on the developer and where the idea came from

You are on the home page with the option to choose by clicking on what type of animal you're interesting in helping from the following choices- Carnivore Herbivore Omnivore

Animal Type Page then will display all of the animals that are in the category you've picked that we have sources for.

Animal Species Page will display the species of the animal you have picked along with a url launch to the animal sources page that has a list of the organizations that aid that species.

Animal Sources page has a list of names of organizations with the link to launch their site to so you can start to be proactive in the help to fight for animals who can't defend themselves in a human dominant world.

The Search Page is an option to find out if the animal or species you're looking for is avaliable on the website.

How to run the program
FOLLOW THIS QUICK TECHNICAL SET-UP SO YOU CAN START USING IT:
1.CREATE AND RUN A VIRTUAL ENVIRONMENT USING VENV: A) first: mkdir [name of your directory]

B) second: [name of your directory]

C) then: clone into directory: https://github.com/DDavis-CP/SaveASpecies2.0.git

D) next: python -m venv django-env (or python3 -m venv django-env)

E) now: (Windows users) django-env\Scripts\activate.bat

(Bash users) source django-env/Scripts/activate

(Unix or MacOS) source django-env/bin/activate

2.INSTALL PROJECT DEPENDENCIES WITH PIP: A) here: pip install django

3.RUN THE DJANGO APLICATION: A) do: pip freeze > requirements.txt

B) execute: python manage.py runserver

C) finally:click on the link with ctrl + right click http://127.0.0.1:8000/