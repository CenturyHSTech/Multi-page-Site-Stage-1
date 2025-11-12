# My Website Project
Apply your new-found web design markup and styling skills by creating a 4-page website based on one of the options described in the assignment.

- Environment Set Up
- Coding Your Project
- Required Elements

---


<details>
<summary><strong>VS Code Setup Instructions</strong></summary>

1. Make sure you have python poetry installed (open the Software Center and look for it in apps)
2. Open Command prompt by clicking in the search window and typing `cmd`
3. Type `poetry --version` - if it gave you a version, you are ready. If not, get the teacher to show you.
4. Make sure you add the Python Extension (the one with the Microsoft seal)
5. Open the terminal (View > New Terminal)
6. Run `poetry env activate` in the terminal
7. Note your virtual environment name
8. Open the Command Palette (`Ctrl + Shift + P`)
9. Select the Python interpreter (look for the Poetry environment)
10. Run `poetry update`
11. Run `pytest` to test your code - it will give you an error (that's to be expected)
12. Create a file named `index.html` into the `project` folder
13. Follow in class instructions on how to code your html file.
14. Review the [Project Requirements](project-requirements) for the assignment
15. Commit and push changes regularly
16. As you work, try typing `pytest` in the terminal to see what tests you are passing and which ones you are failing
17. If you don't know what a failed test means, talk to your teacher to help you work through it.
18. To get a 3/4 proficient in HTML, you need to pass all `test_html.py` tests.
19. To get a 4/4 exceeds, you need to pass all tests (`test_html.py` and `test_html_exceeds.py`).
20. Make sure you push all commits to receive a score.

</details>

---

<details>
<summary><strong>Coding Your Project</strong></summary>

Once the environment is set up, and you're ready to code...
## HTML Structure
1. Create a file named `index.html` in the `project` folder.
2. Follow teacher instructions on creating your web page.
3. Be sure to name your file in the title tag.
4. Be sure to include all required tags for any web page (see the [list of required elements](#required-elements) to make sure you meet minimum requirements).
5. Determine a layout for your page by creating a wireframe or mockup.
6. From that layout determine which HTML5 sectioning content (`header`, `main`, `nav`, `footer`, `article`, etc.) you will use and where.
7. Add content for the home page first by including sample information about each of the other pages (usually a heading that links to the page, some paragraphs of text and an image to go with it followed by a horizontal rule).
8. To save time, I give you permission to get content from other websites or even use AI to generate text content, but ***you DO NOT have permission to have AI generate `HTML` markup, `CSS`, or `JavaScript`***.
9. All content that you do not write yourself MUST be cited either in the footer or after the information you gathered.
10. Create the navbar in the homepage and code it with all the links ready to link to your other pages.
11. Once you think the home page is ready, run it through the [W3C Validator](https://validator.w3.org/#validate_by_upload) and fix any errors before you proceded.
12. Once there are no errors, use the home page (i.e. `index.html`) as a template to create your other pages.
13. Keep all filenames short: one or two words (using hyphens like `about-us.html`)
14. Build out your content.

## CSS 
At any point after creating your initial `index.html` file, you can link to and begin styling.
* Make sure all pages in your site link to the same stylesheet or stylesheets.
* Start by styling the body with color and typography. 
* Your instructor will guide you into creating layouts for your page.
* I recommend a big photo banner for the page and a 1-column centered layout.
* I also suggest a color palette that you generate using `CSS variables` for the colors.

## Testing the project
There are three crucial steps to perform before running the tests on your project:
1. You must run `poetry env activate` and `poetry update`
2. You must install the Python extension and set the Python interpreter (in `View > Command Palette > Python: Select Interpreter`)
3. There needs to be an `HTML` document in the `project` folder.
Once you've done that, try clicking on the Testing icon (it's a beaker/flask icon) and clicking the run icon.

*NOTE: as you are coding your page, be sure to check your page for errors from time to time using the [W3C File Upload Validator](https://validator.w3.org/#validate_by_upload) or through pytest*

</details>

---

<details>
<summary><strong>Required Elements</strong></summary>

* Standard HTML Tags - there should be one for each page (no more no less)
    - `DOCTYPE`
    - `html`
    - `head`
    - `title`
* Required Semantic Layout Elements
    - `header` - at least one
    - `nav` - at least one
    - `main` or `article` - at least one or a combination
    - `footer` - at least one
* Optional Semantic Layout Elements (at least 2 of the following for the win) 
    - `hgroup` - at least one used appropriately
    - `section` - where appropriate
    - `aside` - probably best for a pullout quote
* Other required tags (see minimum #)
    - `h1` -> one per page (in the header)
    - `nav`  -> one (could be in the header or by itself)
    - `ul` -> at least one per page (inside the nav)
    - `li` -> at least 4 per page (inside the ul that's in the nav)
    - `a` -> at least 4 per page (inside each li inside the ul that's in the nav)
    - `h2` -> two (in the section or article)
    - `p`  -> at least 5 per page (in the section or article and at least 1 in the footer)

### Validity Requirements
* No HTML errors are allowed

### CSS Requirements
* Do NOT use style attributes in your HTML - only use a style tag in the head or an external stylesheet.
* Fonts:
    - Apply either a font or font-pair other than Times New Roman or Comic Sans
    - IMPORTANT NOTE ON TYPOGRAPHY AND READABILITY: 
        + in design, the font you choose might hurt readability
        + avoid making all paragraph text bold because it makes content difficult to read 
        + all bold test doesn't highlight key information effectively. 
        + Instead, use bolding sparingly for emphasis on important words or phrases, balance it with regular text, and use semantic HTML like `<strong>` for accessibility. 

* Colors:
    - ALL COLORS must meet [WebAIM color contrast](https://webaim.org/resources/contrastchecker/) goals at the ***"WCAG AAA"*** rating
    - Apply a **background color** to the page (through the body or html)
    - Apply a **color** to the text (through the body or html)
    - Apply a **color** to hyperlinks (to both the link and visited - hover is optional)
    - Add **padding** to any of the following layout elements if present (`header`, `nav`, `main`, `article`, `aside`, `hgroup` `section`, `footer`).

NOTE: to check for errors, be sure to upload your HTML file to the [W3C File Upload Validator](https://validator.w3.org/#validate_by_upload)

</details>