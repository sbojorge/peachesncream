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
