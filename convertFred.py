# le plus dur c'est le commencement, lance-toi ;-)
from markdown import markdown
import sys
import os
import shutil
from jinja2 import Environment, FileSystemLoader
import venv 



source = "./input/images"
destination = "./output/images"
shutil.copytree(src = source, dst = destination)

# ouvrir un fichier
path = "./input/content"
dirs = os.listdir( path )
# This would print all the files and directories
for file in dirs:
    toto = file
    tata = toto.replace('md', 'html')
    #print(tata)
    with open("./input/content/"+toto, "r", encoding="utf-8") as input_file:
        md = markdown(input_file.read())
    with open("./output/"+tata, "x", encoding="utf-8") as output_file:
        temp = Environment(loader=FileSystemLoader(searchpath='./')).get_template("template.html")
        output_file.write(temp.render(content = md))
    
venv.create('./output')


