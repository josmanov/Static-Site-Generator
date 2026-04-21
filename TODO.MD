
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
            [] use extract title function to grab title of page
            [] replace the {{ Title }} and {{ Content }}
                placeholders in template with html and title generated
            