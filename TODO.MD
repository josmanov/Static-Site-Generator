
CH4 L3
    block.py:
        [x] complete heading_to_html(text) function
        [x] complete code_to_html(text) function
        [x] complete quote_to_html(text) function
        [x] complete unordered_to_html(text) function
        [x] complete ordered_to_html(text) function
        [x] compelte paragraph_to_html(text) function:

CH5: L1
    Write a function that copies all contents from src dir to dest dir 
    (static to public):
        [x] first delete everything from public
        [x] copy all files and folders, nested folder into public
        [x] log path of each file thats copied for debugging
        [x] hook function to main function and test manually with file system
        [x] add public directory to .gitignore file.
        [x] check main.sh generates the public dir and everything is copied correctly
        [x] fix wrong path for index.css file

CH5: L2
    Generate and serve a webpage:
        [x] Create a function that extract title from markdown
        [x] write test unit for it
        [x] create a function that generage the page using a src_path the template path and dest_path
            [x] print message "generating page from {src_path} to {dest_path} using {template_path}"
            [x] read markdown file at from path and store contents
            [x] read the template file at template_path and store contents
            [x] use markodwn to html node function and to_html method to convert markdown file to html string
            [x] use extract title function to grab title of page
            [x] replace the {{ Title }} and {{ Content }}
                placeholders in template with html and title generated
            [x] write new full html page to file at      {dest_path}, create necessary dirs if not existing
        [x] update main.py to  generate a page from content/index.md using tempalte.html to write to public/index.html
        [x] main.sh script should start a web server after generating the site, same as before

CH5:L3
    Create more pages:
        [x] add following markdown files:
            * content/blog/glorfindel/index.md
            * content/blog/tom/index.md
            * content/blog/majesty/index.md
            * content/contact/index.md
        [x] add images from bootdev into static/images dir
        [x] run generator to copy from static to public dir

CH5:L4
    Recursvely generate pages using dir path content template path and dest dir path:
        [x] crawl into every entry in content directroy
        [x] each markdown file found, genereate new .html file using template
        [x] write them into public dir in same structure
        [x] update main to use recursion instead of one page generation
        