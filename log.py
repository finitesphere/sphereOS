# Python log posting script

# Importing BeautifulSoup, subprocess, and datetime modules
from bs4 import BeautifulSoup
from datetime import datetime
import subprocess

now = datetime.now()
current_date = now.strftime(" | %B %d, %Y %I:%M:%S %p")

def log():
    with open('updates.html', 'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

        print("What is the title of the post?")
        title = input("").title()

        # log Post Title
        log_title = soup.new_tag('h2', attrs={'id':'log-post-title'})
        log_title.string = title + current_date

        print("Type out the post")
        content = input("")

        # log Post Content
        log_content = soup.new_tag('p', attrs={'id':'log-post'})
        log_content.string = content

        print("Do you want to submit the post? (Y/N)")
        submit = input("").upper()
        if "Y" in submit:
            print("Submitted")
        elif "N" in submit:
            exit()
        else:
            print("Do you want to restart the post? (Y/N)")
            answer_restart = input("").upper()
            if "Y" in answer_restart:
                log_post()
            else:
                exit()
        
        # Formats the blog-post-title before the blog-post-content
        soup.html.body.h2.insert_before(log_content)
        soup.html.body.p.insert_before(log_title)

        soup.prettify()
        
        # Using neocities to host the static blogpost website
        # You will have to be in the working directory as the script, html, and css are located in. You will also need to change the cwd.
        
        #subprocess.call('neocities push -e log.py .', shell=True, cwd="/home/USER/log_website")

        with open("updates.html", "w", encoding = 'utf-8') as file:
            file.write(str(soup.prettify()))
log()
