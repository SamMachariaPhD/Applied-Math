# add a php line as the very first line of the html doc 
# save the new doc as php
# change comments identifier and reference name 
# Sam Macharia, PhD

from pathlib import Path

file_title = input("\n=> Enter only the <name> of the <name>.html file: ")
html_file = file_title +".html"
php_file = file_title +".php"
string = "<?php session_start(); ?>"

def insert(html_file,string):
    with open(html_file,'r') as f:
        with open(php_file,'w') as f2:
            f2.write(f'{string}\n')
            f2.write(f.read())

insert(html_file,string)

file = Path(php_file)
file.write_text(file.read_text().replace("$cmtx_identifier = '1';", "$cmtx_identifier = '"+file_title+"';"))
file.write_text(file.read_text().replace("$cmtx_reference  = 'Comments';", "$cmtx_reference  = '"+file_title+"';"))
