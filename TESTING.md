## Manual Testing
### Functional Testing

#### Landing page (available for unauthenticated users)
Links related to the app (in the navbar) and those to social medias (in the footer) :
 * Create list > redirects to the Sign in page
 * Sign up > once the Sign up form is completed, redirects the user to the "Create a shopping list" page.
             There is also a link to Sign in which works well too.
 * Sign in > once the Sign in form is completed, redirects the user to the "Home" page.
             There is also a link to Sign up which works well too.
 
 all of them work as expected.
 The same links are available for small devices and work well too.

 #### Authenticated users navbar
 Links for authenticated users:
 * Home > redirects the user to a personal home page.
 * Logout > redirects the a "Sign out confirmation" page in which the "Sign out" buttons works as expected.
 * Add list > redirects the user to the "Create a shopping list" page.
 * My list > redirects the user to the list of created shopping lists page.
 * Contact > redirects the user to the contact form page.

 all of them work as expected.
 The same links are available for small devices and work well too.

 #### Home page
 The name of the user is correctly displayed in a welcome message.

 There are 2 links available in this page depending on the number of created shopping lists:
 * Lists links, for user with 1 or more saved lists,
 * Add link, for users with 0 saved lists.

 Both links work properly.

 #####  CRUD functionality (shopping list)
 Manual testing of the CRUD functionality, including the followed steps, is described below:

 ##### Create a shopping list:
 1. On the navbar, click on "Add list".
 A form is displayed. Fill in the blanks:
 2. Give a name to the shopping list (optional).
 3. Choose a category for the shopping list from the select menu.
 4. Type the name of the shop where you'd like to buy (optional).
 5. Add the items to buy. User can add quantity, brand or any other comment next to the item.
    Widgets are available (number list, bullets, Undo, Redo, Fullscreen).
 6. Click on the "Create list" button.

 Expected: A success message should be displayed to the user and the list should be registered in "My lists".

 Actual: The success message is correctly displayed and automatically dismissed. The newly created list is saved.

 ![add1](/static/images/test/CRUD/picture_1.png)

 ![add2](/static/images/test/CRUD/picture_2.png)

##### Read/Retrieve a list of owned shopping lists:
 1. On the navbar, click on "My lists".
 The list of owned existing shopping lists is displayed along with an "Add" button in case the user would like to create a new one. 
 2. Click on the name of any of the lists to read/retrieve its detail.
 3. The user is redirected to the corresponding grocery_list/id template and a card with the list data is displayed on the UI.
 4. Edit and Delete buttons are available at the bottom of the card.

 Expected: The list of existing shopping list should be displayed and all lists should be clickable.

 Actual: The list of existing shopping list is displayed and all lists are accesible.
 
 ![read1](/static/images/test/CRUD/picture_3.png)

 ![read2](/static/images/test/CRUD/picture_4.png)

A security check has been added here so user can't access someonelse shopping list via the URL:

![read3](/static/images/test/CRUD/picture_5.png)

These security check is also applicable for editing and deleting functionalities.

##### Edit an owned shopping list:
 1. Once on the grocery_list/id template, click on the "Edit" icon.
 The user is redirected to the grocery_list/edit/id template which displays the same form that the user filled in when creating the shopping list.
 2. After editing the field of your choice, click on the "Update list" button available at the bottom of the form. 

 Expected: A success message should be displayed and the use should be redirected to the list of owned existing shopping lists.

 Actual: The success message is correctly displayed and automatically dismissed. The list of shopping lists is displayed.
 
 ![edit1](/static/images/test/CRUD/picture_6.png)

 User can't edit someone else's list:

 ![edit2](/static/images/test/CRUD/picture_7.png)

 ##### Delete an owned shopping list:
 1. Once on the grocery_list/id template, click on the "Delete" icon.
 The user is redirected to the grocery_list/delete/id template.
 2. Confirm that you want to delete the list by clicking on the available "Delete list" button. 

 Expected: A success message should be displayed and the use should be redirected to the list of remaining owned shopping lists.

 Actual: The success message is correctly displayed and automatically dismissed. The list of remaining shopping lists is displayed.
 
 ![delete1](/static/images/test/CRUD/picture_8.png)

 ![delete2](/static/images/test/CRUD/picture_9.png)

 User can't delete someone else's list:

 ![delete3](/static/images/test/CRUD/picture_10.png)

#####  CRUD functionality (contact form)
Manual testing of the CRUD functionality, including the followed steps, is described below:

 ##### Create a contact form:
 1. On the navbar, click on "Contact".
 A form is displayed. Fill in the blanks:
 2. The reason of the contact (required).
 3. The content of the message that you want to send (required).
 4. Click on the "Send" button available at the end of the form.
 
 Expected: A success message should be displayed to the user and the list should be registered in the backend.

 Actual: The success message is correctly displayed and automatically dismissed. The contact is saved.

 ![contact1](/static/images/test/CRUD/picture_11.png)

 Retrieve, Update and Delete functionalities are available only at admin level and can be performed by superusers.

 1. Navigate to the admin site. The "Contacts" table is available on the left hand menu.

  ![contact2](/static/images/test/CRUD/picture_12.png)
 
 From here Retrieve, Update and Delete actions can be perform.

 ##### Retrieve an existing contact form:
1. Click on "Contacts".
2. The list of existing contacts is displayed.
3. Click on any of them to see its detail.

 ##### Update an existing contact form:
1. After clickin on a contact form, the superuser is redirected to the /admin/contact/contact/id/change/ page.
2. Modify any of the fields and click on save.
3. A succes message is displayed and the superuser is redirected to the list page.

![contact3](/static/images/test/CRUD/picture_13.png)

##### Deleting an existing contact form:
1. Select a contact by checking its box.
2. Click on "Delete selected contacts" from the dropdown menu "Actions".
3. Click on "Go".
4. Confirm that you want to delete the contact.
5. A succes message is displayed and the superuser is redirected to the list page.

![contact4](/static/images/test/CRUD/picture_14.png)

------

## Validators
### W3 Markup Validation Service

Template views (.html files) use the Django template language.
HTML code from these files is the one rendered in the "view page source" and was obtained as follows:
1. Open the page to validate,
2. Right click and 
3. Select "view page source".

Code was tested using the [official markup validation service](https://validator.w3.org/).

A few info messages related to trailing slashes on void elements were shown in the validation results of these pages:
- Landing
- Sign up
- Sign in
- Home
- Delete
- Logout
- 403

![info](/static/images/test/w3c/picture_1.png)

None action was taken because, in the current situation, the following acceptable reason for using trailing slashes applies:

![trailing](/static/images/test/w3c/picture_2.png)

The following pages present 1 error which is mainly due to the fact that forms are styled as paragraphs and the validator doesn't see the opening `<p>` tag:
- Add list
- Edit list
- Detail list

![ptag](/static/images/test/w3c/picture_3.png)

"My lists" page has 2 errors that are irrelevant because the closing tags are correctly situated:

![errors](/static/images/test/w3c/picture_4.png)

![code](/static/images/test/w3c/picture_5.png)

Finally, the "Contact" page has 1 error which is due to CSS in the materializecss module:

![contacterror](/static/images/test/w3c/picture_6.png)

![contactcode](/static/images/test/w3c/picture_7.png)

### W3 CSS Validation Service

CSS was validated using the [official validator ](https://jigsaw.w3.org/css-validator/validator.html.en) and this is the result:

![css](/static/images/test/w3c/picture_8.png)

### CI Python Linter

The code that I wrote on each app (admin, models, urls, views, forms) was validated using the [CI Python Linter service](https://pep8ci.herokuapp.com/) and this is the result:

![python](/static/images/test/python/picture_1.png)

------

## Accesibility

[Wave Accessibility](https://wave.webaim.org/) tool was used for accessibility testing.

The majority of the pages are free of errors:

![waver1](/static/images/test/wave/picture_1.png)

![waver2](/static/images/test/wave/picture_2.png)

![waver3](/static/images/test/wave/picture_3.png)

![waver4](/static/images/test/wave/picture_4.png)

There are contrast errors in the pages with forms, but this is due to the style applied by materializecss.min.css which I can't change so no further action was taken.

![waver5](/static/images/test/wave/picture_5.png)

------

## Lighthouse report

Web page quality was test using the [Google Lighthouse service](https://developer.chrome.com/docs/lighthouse/overview/) and this is the result:

![lighthouse](/static/images/test/lighthouse/picture_1.png)

------

## Responsiveness

The website is responsive in the most common screen devices (smartphone, tablet, laptop and desktop) and within the following width categories:

* 320 x 480px
* 768 x 1024px
* 1280 x 802px
* 1600 x 992px

No loading issues nor pixelated or streched  images across Chrome, Edge, Safari.

Follow this link to go back to the main [readme document.](/README.md)