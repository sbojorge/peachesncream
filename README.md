![Peachesncream logo](/static/images/logo/picture_1A.webp)

# Peaches 'n cream


Peachesncream is a shopping list web application.<br>
It'll be useful for users searching to organize their trips for any kind of shopping i.e groceries, wishlists, gifts etc.<br>
The application lets the user to perform all the CRUD functionalities on shopping lists.<br>
Lists won't be losts, items won't be forgotten, but instead the user will be able to access it from his/her mobile.<br>
<br>

<!-- Add an image of the responsive app here and underneath this the link to the deployed app. -->

## Contents
<!-- I've writen this content for helping to organize and follow the README and TESTING content. As GitHub creates automatically a table content after 2 or more headings, I'll probably delete this content once the README will be completed. -->

1. [Technologies](#technologies)
2. Methodology
    - Themes, Epics and User stories
    - Backlog refinement
    - Kanban board    
3. Design
    - Database schema
    - Wireframes (Mobile and desktop)
    - Typography
    - Colors
    - Images?
4. Features
    - Existing features
    - Features to be implemented
5. Testing
    - Markdown validator
    - CSS validator
    - JS Hint
    - CI Python linter
    - Responsiveness
    - Accesibility
    - Lighthouse
    - Manual and/or Automated testing
6. Deployment
7. Credits
    - Content
    - Media
8. Acknowledgments

[Back to top 🔺](#peachesncream)

------

### Technologies
<!-- Currently showing here some examples of technologies that I'll probably use. Develop a bit for each of them as shown below for balsamiq -->
* HTML
* CSS
* JavaScript
* Django
* Django Allauth
    * Authentication and authorisation were done using [Django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html)
* Django Crispy forms
* Django RichTextField
    * Text editor for assisting the user to create the grocery shopping lists and add widgets
* Materialize
* GitHub
* Convertio
    * Images were converted to WEBP format using [Convertio](https://tinyjpg.com/) 
* Resize
    * Images were resized using [Resizepixel](https://www.resizepixel.com/)
* TinyJPG
    * Images were compressed using [TinyJPG](https://tinyjpg.com/)
* Favicon.io    
* Balsamiq
    * Wireframes were created using [Balsamiq Wireframes for desktop](https://balsamiq.com/wireframes/desktop/)
 * Canvas
    * For creating the logo at [Canvas](https://www.canva.com/)

[Back to top 🔺](#peachesncream)

------

### Methodology
The methodology used in this project is the Kanban Agile management methodology.

It was put in place using different functionalities in GitHub: 
* Issues, for the user stories; <!-- add pic -->
* Milestone (without due date), for the product backlog; <!-- add pic -->
* Milestone (WITH due date), for each iteration; <!-- add pic -->
* Project, for the Kanban board. I created a project per iteration. <!-- add pic -->
> Kanban is an Agile management method built on a philosophy of continuous improvement, where work items are “pulled” from a product backlog into a steady flow of work. The framework is applied using Kanban boards—a form of visual project management. In a Kanban board, tasks—represented as cards—move through stages of work—represented as columns...“To do,” “In progress,” and “Done.” Each column is filled with visual cards that represent individual tasks. A team moves through the columns until the tasks are completed.

<!-- Add a project picture here. -->

------

[Back to top 🔺](#peachesncream)

### Design
#### Database schema

* Model

![Grocery model](/static/images/db_schema/picture_1.png)

#### Wireframes
* Landing page

![Browser landing page](/static/images/wireframes/picture_1.png)

![Mobile landing page](/static/images/wireframes/picture_2.png)

* Create a grocery shopping list

![Browser create a list](/static/images/wireframes/picture_3.png)

![Mobile create a list](/static/images/wireframes/picture_4.png)

* Display the list of created grocery shopping lists

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

#### Images

------

[Back to top 🔺](#peachesncream)

### Features

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

### Testing

Links to social media and those related to the app:
 * Home
 * Sign up
 * Sign in 
 * Create list
 * Add list
 * Edit list
 * Delete list
 
 all of them work as expected.

* Accesibility

![Wave accesibility results](/static/images/test/wave_result_landing.png)

There is a warning in the Wave accesibility report and this is related to missing headings in the structure of the page, but in the design none heading is necessary.

------

### Deployment

The application was early deployed following these steps:

* Prepare environment and settings.py file
    -   create env.py,
    -   secret key,
    -   database url and update the database section,
    -   cloudinary url, link Cloudinary to the application for storing media and static files and add the cloudinary apps in the installed apps section
    -   templates including creating the corresponding directory, 
    -   allowed host,    
    
* Create an external database on ElephantSQL and attach it to the application
* Create an application on Heroku and prepare the configuration variables on it
    -   secret key
    -   database url
    -   cloudinary url
    -   port
    -   disable collectstatic

* Create media and static directories
* Create and prepare a procfile
* Connect the repository to the Heroku app and deploy branch

The application was successfully deployed at the first attempt.

#### Bug


### Credits


* The security check added to the Display_item view was inspired on [Securing Django Views from Unauthorized Access](https://www.codu.co/articles/securing-django-views-from-unauthorized-access-npyb3to)

* Adding the LoginRequiredMixin in the EditList view comes from [Django Recipe Sharing Tutorial - 13. Edit Recipe](https://www.youtube.com/watch?v=JzDBCZTgVyw&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=14)

* Adding and displaying messages to users inspired on [Messages-Django Tutorial](https://pythonprogramming.net/messages-django-tutorial/?completed=/user-registration-django-tutorial/)


#### Media
* The image for creating the logo comes from [Shutterstock](https://www.shutterstock.com/)
* Fonts from https://fonts.google.com/ following the article published by Canva at https://www.canva.com/learn/best-google-font-combinations/
* Color palette from https://mycolor.space/

#### Content
* Quotation about the Kanban management methodology: visit https://asana.com/resources/what-is-kanban

### Acknowledgments

Always and in first place to my loving and supporting family.

Huge thanks to my mentor, Daisy McGirr for her guidance and professionalism.

[Back to top 🔺](#peachesncream)
