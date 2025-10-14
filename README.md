# My Website Project
Apply your new-found web design markup and styling skills by creating a 4-page website based on a topic of your choice.


- Environment Set Up
- Coding Your Project
- Required Elements

---


<details>
<summary><strong>Environment Set Up</strong></summary>

Getting your project up and running in VS Code.
1. Clone this project: `git clone`.
2. Open the project in VS Code (double click on `About-Me-HTML-Part-1.code-workspace`)
3. Open the terminal (View > New Terminal).
4. Install the Python extension: ***Python extension for Visual Studio Code***
5. In the terminal, type `poetry shell`.
    - You should see a line saying something like `Spawning shell within C:\Users\my_username\AppData\Local\pypoetry\Cache\virtualenvs\simple-html-page-IMtvp_MA-py3.9`
6. Note the name of your virtual environment file, which will look something like `simple-html-page-IMtvp_MA-py3.9`
7. Open the Command Palette 
    - in the menu it's: View > Command Palette
    - you could also type `Ctrl + Shift + P`
8. Type Python: Select Interpreter
    - if you see the virtual environment file, click it.
    - if you don't see it, click `Select at Workspace level`
9. Select the virtual environment file from above (it should show the word Poetry in blue on the right)
    - if you don't see it, close VS Code and re-open it and repeat steps 8 and 9.
10. Type `poetry update` and wait for everything to install.
11. In the terminal, once everything is done installing, type `pytest`
12. If that doesn't work, click the Testing icon (looks like a beaker), then click the blue `Configure Python Tests` button, then select `pytest pytest framework` and choose the `tests` folder
13. If that still doesn't work, ask your teacher to help you out.
14. Follow the steps in [Coding Your Project](#coding-your-project).
15. At key stopping points (usually once you test something in the browser and you like it), it's time to commit and push your changes like so...
    * `git add *`
    * `git commit -m "fixing/editing/adding ______"`
    * `git push origin main`
16. If you want to see if you are doing it right, check your code by typing `pytest`.
17. Once you think you're done, save your changes, make one last commit and push, and turn in your assignment by clicking the "Mark as Done" button.

</details>

---

<details>
<summary><strong>Coding Your Project</strong></summary>

Once the environment is set up, and you're ready to code...

1. Create a file named `index.html` in the `project` folder.
2. Follow teacher instructions on creating your web page.
3. Be sure to name your file in the title tag.
4. Be sure to include all required tags for any web page (see the [list of required elements](#required-elements) to make sure you meet minimum requirements).
5. Create the following layout elements for your page:
    * A `<header>` at the top with your title (`<h1>` and a tagline `<p>` inside.)
    * A `<nav>` element with an unordered list of links to each page including the home page as well as the other pages (at least 3 other pages).
        - That means a minimum of 4 `<li>` elements each with at least 1 `<a>` element that uses a relative link to each page
        - IMPORTANT: every page in your site needs to include the nav AND ***every nav must include the same links in the same order (even when they are linking to the same page they are on).***
    * Either a `<section>` or an `<article>` for the main content of each page.
    * A `<footer>` element at the bottom to put any credits (to yourself as well as any sources for images or text)
6. Inside the `<section>`, you will need the following tags:
    * At least 2 `<h2>` elements.
    * At least 4 `<p>` elements.
    * At least 2 `<figure>` elements for images with 1 `<img>` and a `<figcaption>` with a description or title for the image.
    * No matter what styles you provide...
        - ***everything must be readable***
        - ***no text should be touching a border or edge of the screen***
8. For more specific information on how to pass test, please refer to the README file in the project folder.

*NOTE: as you are codign your page, be sure to check your page for errors using the [W3C File Upload Validator](https://validator.w3.org/#validate_by_upload)*

</details>

---

<details>
<summary><strong>Required Elements</strong></summary>

* Standard HTML Tags - there should be one for each page (no more no less)
    - `DOCTYPE`
    - `html`
    - `head`
    - `title`
* Other required tags (see minimum #)
    - `h1` -> one per page (in the header)
    - `header` -> one per page
    - `nav`  -> one (could be in the header or by itself)
    - `ul` -> at least one per page (inside the nav)
    - `li` -> at least 4 per page (inside the ul that's in the nav)
    - `a` -> at least 4 per page (inside each li inside the ul that's in the nav)
    - `section` OR `article` -> at least 1 per page
    - `h2` -> two (in the section or article)
    - `p`  -> at least 5 per page (in the section or article and at least 1 in the footer)
    - `footer` -> at least 1 per page

### Validity Requirements
* No HTML errors are allowed

### CSS Requirements
* Do NOT use style attributes in your HTML - only use a style tag in the head or an external stylesheet.
* Colors:
    - ALL COLORS must meet [WebAIM color contrast](https://webaim.org/resources/contrastchecker/) goals at the following levels:
        * Headings must at least meet ***"WCAG AA"*** rating
        * Body text (table content and links included) must meet ***"WCAG AAA"*** rating
    - Apply a **background color** to the page (through the body or html)
    - Apply a **color** to the text (through the body or html)
    - Apply a **color** to hyperlinks (to both the link and visited - hover is optional)
    - Apply a **background color AND color** to the `figure`
    - Apply a **styled border** around the `figure`
    - Add **padding** to all layout elements (`header`, `nav`, `article` or `section`, `footer`).

NOTE: to check for errors, be sure to upload your HTML file to the [W3C File Upload Validator](https://validator.w3.org/#validate_by_upload)

</details>