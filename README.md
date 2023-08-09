![Peachesncream logo](/static/images/logo/picture_1A.webp)

# Peaches 'n cream

Peachesncream is a shopping list web application.<br>
It'll be useful for users searching to organize their trips for any kind of shopping i.e groceries, wishlists, gifts etc.<br>
The application lets the user to perform all the CRUD functionalities on shopping lists.<br>
Lists won't be losts, items won't be forgotten, but instead the user will be able to access it from his/her mobile.
<br>

Please click here to visit the deployed site [Peachesncream](https://newpeachesncream.herokuapp.com/)

![Responsiveness](/static/images/design/picture_3.png)

------
 
[Back to top 🔺](#peachesncream)

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

> Kanban is an Agile management method built on a philosophy of continuous improvement, where work items are “pulled” from a product backlog into a steady flow of work. The framework is applied using Kanban boards—a form of visual project management. In a Kanban board, tasks—represented as cards—move through stages of work—represented as columns...“To do,” “In progress,” and “Done.” Each column is filled with visual cards that represent individual tasks. A team moves through the columns until the tasks are completed.

The methodology was put in place using different functionalities in GitHub: 
* Issues, for the user stories;
* Milestone (without due date), for the product backlog;
* Milestone (WITH due date), for each iteration;
* Project, for the Kanban board.

![project](/static/images/agile/picture_1.png)

------

[Back to top 🔺](#peachesncream)

## Design
### Database schema

The database is composed of 3 models (2 are customised, which meets the assessment criteria of a "minimum of one custom model"): 

- User,
- Grocery_list,
- Contact.

The User model is at center, being connected to the 2 others by the id.<br>
There isn't any direct relation between the Grocery_list and Contact models.

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

### Landing page
This is the cover of the application.<br>
Logo and a brief explanation about the purpose of the app can be found here as well as a Sign up button.

![Landing page on desktop](/static/images/features/picture_1.png)

![Landing page on mobile](/static/images/features/picture_2.png)

The page also includes:

#### Navigation bar
This element has 3 links for unauthenticated users: Create list, Sign up and Sign in.

![Desktop navbar](/static/images/features/picture_3.png)

And 5 links for authenticated users: Home, Logout, Add list, My lists and Contact.

![Desktop navbar](/static/images/features/picture_3a.png)

On medium and small devices, the navigation is collapsed into a hamburguer icon:

![Hamburguer icon](/static/images/features/picture_4.png)

When the user clicks on that icon, the content of the navigation bar is displayed:

![Navbar mobile](/static/images/features/picture_5.png)

#### Footer
This section, which is present in all pages of the application, holds social media icons to the GitHub and LinkedIn profiles of the developper:

![Footer](/static/images/features/picture_6.png)

### Authentication pages:
#### Sign up
Users can create an account by clicking the Sign up button and completing the form:

![signup](/static/images/features/picture_9.png)

Warnings are displayed to the user in case of error:

![signup](/static/images/features/picture_9a.png)

After signing up, the user is redirected to the [Create shopping list](#addlist).

#### Sign in
Users can access their account, create and manage their shopping list by clicking the sign in button and completing the form:

![signin](/static/images/features/picture_10.png)

Warnings (color and text) are displayed to the user in case of error:

![signin1](/static/images/features/picture_11.png)

After signing in, a sucess message is displayed to the user and he/she is redirected to the Home page:

![signin2](/static/images/features/picture_11a.png)

The success message feature is also available upon submission of a valid form when:
- adding a shopping list,
- editing a shopping list,
- deleting a shopping list and
- logging out.

### Home page
A welcome message including the username of the authenticated user is displayed along with the number of the owned existing shopping lists (if any) and a button to access them.

![Home1](/static/images/features/picture_8.png)

If the user doesn't have any list the displayed button can redirect him/her to the "Create a shopping list" page:

![Home2](/static/images/features/picture_7.png)

### CRUD pages
#### Add list (Create shopping list page)
The authenticated user can create here any kind of shopping lists by completing the form and hitting the "Create button" at the end.<br>
The form has the following fields:
- Name of the list (optional), which has "My shopping list" as placeholder,
- Category (optional), which has "Groceries" as placeholder,
- Shop (optional), so the user can register where to buy/pick up the products,
- Items (required), user can add quantity, brand or any other comment next to the item.<br>
Widgets are available (number list, bullets, Undo, Redo, Fullscreen).

![add1](/static/images/features/picture_12.png)

![add2](/static/images/features/picture_12a.png)


#### My lists (My shopping lists page)
The authenticated user can retrieve the list of his/her owned shopping lists by clicking on "My lists" on the navbar.<br>
Shopping lists are displayed in descending order.<br> An "Add" button (plus icon) is available as well in case the user wants to create a new list:

 ![read1](/static/images/test/CRUD/picture_3.png)

#### Edit a shopping list
From the displayed list of owned shopping list, the user can see the detail of any list by clicking on its name.<br>
An "Edit" button (pencil icon) is available.<br>

![edit](/static/images/features/picture_14.png)

#### Delete a shopping list
In case the user wishes to delete the displayed list, the "Delete" button (trash icon) is available on this same page.

![delete1](/static/images/features/picture_15.png)

#### Delete confirmation page
In order to prevent undesired deletion, a  delete confirmation page feature is provided:

![delete2](/static/images/features/picture_15a.png)

### Contact
This feature is available for letting the user communicate with the developer which maintain the application.
It can be used for suggestions, concerns, etc:

![contact](/static/images/features/picture_16.png)

### Preventive actions
#### 403 page
The user is unable to perform RUD actions (read, update, delete) on other user's shopping list.
In case a user tries to access someone else shopping list, he/she is redirected to the 403 page:

![403](/static/images/features/picture_17.png)

#### Accesing the Sign up after logging in
Authenticated users can't access the landing page nor the Sign up button via the URL:

![redirects](/static/images/features/picture_17a.png)

### Sign out
When clicked, the "Logout" link, redirects the user to a "Sign out confirmation" page.<br>
If confirmed, the user will be logged out.

![signout](/static/images/features/picture_18.png)

------

[Back to top 🔺](#peachesncream)

## Features to be implemented

1. Forgot password, as an aid to the sign in.
2. An item category, so products can be better organized.
3. A shop app, so users can create/add their favorite shops and details
4. A cancel button for actions like adding, updating or deleting a shopping list
5. Sharing lists with other users (like family members) so they can see/edit the shopping list as well.

------

## Testing
Follow this link for the documentation related to [tests](/TESTING.md).

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
