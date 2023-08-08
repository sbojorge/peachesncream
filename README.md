![Peachesncream logo](/static/images/logo/picture_1A.webp)

# Peaches 'n cream

Peachesncream is a shopping list web application.<br>
It'll be useful for users searching to organize their trips for any kind of shopping i.e groceries, wishlists, gifts etc.<br>
The application lets the user to perform all the CRUD functionalities on shopping lists.<br>
Lists won't be losts, items won't be forgotten, but instead the user will be able to access it from his/her mobile.
<br>

The website is responsive in the most common screen devices (smartphone, tablet, laptop and desktop) and within the following width categories:

* 320 x 480px
* 768 x 1024px
* 1280 x 802px
* 1600 x 992px

Please click here to visit the deployed site [Peachesncream](https://newpeachesncream.herokuapp.com/)

![Responsiveness](/static/images/design/picture_3.png)

Contents (delete after complete documentation)
<!-- I've writen this content for helping to organize and follow the README and TESTING content. As GitHub creates automatically a table content after 2 or more headings, I'll probably delete this content once the README will be completed. -->


2. Methodology
    Epic and User stories     

    
4. Features
    - Existing features (develop)
    - Features to be implemented
5. Testing
    
    
   
    
    - Responsiveness
    - Accesibility
    - Lighthouse
    - Manual and/or Automated testing


[Back to top 🔺](#peachesncream)

------

## Technologies used
The web application was built using Django 3.2.

In addition the following were used for the development of this project:

* HTML
* CSS
* JavaScript
* Django
* [Django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
* [Django Cloudinary](https://pypi.org/project/django-cloudinary-storage/)
* [Django Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
* [Django RichTextField](https://pypi.org/project/django-richtextfield/)
* [Materializecss](https://materializecss.com/)
* [Balsamiq Wireframes for desktop](https://balsamiq.com/wireframes/desktop/)
* [Canvas](https://www.canva.com/)
* [Lucidchart](https://www.lucidchart.com/)

[Back to top 🔺](#peachesncream)

------

## Project management
### Methodology
The methodology used in this project is the Kanban Agile management methodology.

It was put in place using different functionalities in GitHub: 
* Issues, for the user stories;
* Milestone (without due date), for the product backlog;
* Milestone (WITH due date), for each iteration;
* Project, for the Kanban board.
> Kanban is an Agile management method built on a philosophy of continuous improvement, where work items are “pulled” from a product backlog into a steady flow of work. The framework is applied using Kanban boards—a form of visual project management. In a Kanban board, tasks—represented as cards—move through stages of work—represented as columns...“To do,” “In progress,” and “Done.” Each column is filled with visual cards that represent individual tasks. A team moves through the columns until the tasks are completed.

![project](/static/images/agile/picture_1.png)

------

[Back to top 🔺](#peachesncream)

## Design
### Database schema

![db](/static/images/db_schema/picture_1.png)

### Wireframes
* Landing page

![Browser landing page](/static/images/wireframes/picture_1.png)

![Mobile landing page](/static/images/wireframes/picture_2.png)

* Create a shopping list

![Browser create a list](/static/images/wireframes/picture_3.png)

![Mobile create a list](/static/images/wireframes/picture_4.png)

* Display the list of created shopping lists

![Browser display the lists](/static/images/wireframes/picture_5.png)

![Mobile display the lists](/static/images/wireframes/picture_6.png)

#### Typography
A combination of two fonts were used in the desing of the application:<br> 
* "Homemade Apple",in the logo and headings;<br>
* "Raleway",in the body and footer.<br>

This pairing of fonts provides a touch of elegance and clearness to read the rest of the content.

<br>

![Fonts sample](/static/images/design/picture_1.png)
<br>

#### Colors
The selected color palette for in the application comes from a color generator.<br>
This combination in the background colors and fonts adds freshness and respect the minimum contrast values for good accesibility. 

![Natural palette](/static/images/design/picture_2.png)
<br>

------

[Back to top 🔺](#peachesncream)

## Features

The application counts with the following features:

* Landing page

![Landing page on desktop](/static/images/features/picture_1.png)

![Landing page on mobile](/static/images/features/picture_2.png)

* Navigation bar

This element holds 3 links in the landing page: Home, Sign up and Sign in

![Desktop navbar](/static/images/features/picture_3.png)

On medium and small devices, the navigation bar gets collapsed into a hamburguer icon:

![Hamburguer icon](/static/images/features/picture_4.png)

When the user clicks on that icon, the content of the navigation bar is displayed:

![Navbar mobile](/static/images/features/picture_5.png)

* Footer

This section, which is present in all pages of the application, holds social media icons to the GitHub and LinkedIn profiles of the developper:

![Footer](/static/images/features/picture_6.png)

------

[Back to top 🔺](#peachesncream)

## Testing
Follow this link for the documentation related to [tests](/TESTING.md)

------

[Back to top 🔺](#peachesncream)

## Control version

The site was created using GitPod as editor and pushed to Github to the remote repository peachesncream.
### Early deployment

The application was early deployed following these steps:

* Prepare environment and settings.py file
    -   create env.py,
    -   secret key,
    -   database url and update the database section,
    -   cloudinary url, link Cloudinary to the application for storing media and static files and add the cloudinary apps in the installed apps section
    -   templates including creating the corresponding directory, 
    -   allowed host,    
    
* Create an external database on ElephantSQL and attach it to the application.
* Create an application on Heroku and prepare the configuration variables on it:
    -   secret key
    -   database url
    -   cloudinary url
    -   port
    -   disable collectstatic

* Create media and static directories.
* Create and prepare a procfile.
* Connect the repository to the Heroku app.
* Allow the automatic deployment in Heroku so the app is reloaded after each push in the workspace.
* Click on deploy branch.

The application was successfully deployed at the first attempt.

### Final deployment

For the final deployment, the 'X_FRAME_OPTIONS' variable was set in settings.py. This was made with the purpose f letting the text editor (RichTextEditor) to be loaded.

DEBUG was set to False.

### Forking

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.

### Cloning

Cloning is used to create a local copy of the repository created in GitHub.
Both, the local copy and the remote are syncronized.

- Navigate to the GitHub Repository you want to clone.

- Above the list of files, click Code.

There are 3 possibilities for copying the URL of the repository: HTTPS, SSH key and GitHub CLI.
I'll develop the one that I use.

- Click the HTTPS tab and copy the URL.

- On your machine, open your text editor, go to the Command palette and click on Git Clone.

- Past the URL, hit enter and choose a folder to save the repository.

------

[Back to top 🔺](#peachesncream)

## Credits
### Code

* The security check added to the Display_item view was inspired on [Securing Django Views from Unauthorized Access](https://www.codu.co/articles/securing-django-views-from-unauthorized-access-npyb3to)

* Adding the LoginRequiredMixin in the EditList view comes from [Django Recipe Sharing Tutorial - 13. Edit Recipe](https://www.youtube.com/watch?v=JzDBCZTgVyw&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=14)

* Adding and displaying messages to users inspired on:
- [Messages-Django Tutorial](https://pythonprogramming.net/messages-django-tutorial/?completed=/user-registration-django-tutorial/)
- [Show Message in Class-Based Views - Django](https://tech.serhatteker.com/post/2020-11/show-success-message-in-cbv-django/)



### Media
* The image for creating the logo comes from [Shutterstock](https://www.shutterstock.com/)
* Fonts from https://fonts.google.com/ following the article published by Canva at https://www.canva.com/learn/best-google-font-combinations/
* Color palette from https://mycolor.space/

### Content
* Quotation about the Kanban management methodology: visit https://asana.com/resources/what-is-kanban

------

## Acknowledgments

Always and in first place to my loving and supporting family.

Huge thanks to my mentor, Daisy McGirr for her guidance and professionalism.

I'd also like to thank the tutoring team who helped me with debugging.

[Back to top 🔺](#peachesncream)
