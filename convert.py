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


with open("./input/content/create-page.md", "r", encoding="utf-8") as input_file:
    text_md = input_file.read()
    html = markdown(text_md)
    #print(html)
temp = Environment(loader=FileSystemLoader(searchpath='./')).get_template("template.html")
var1 = temp.render(content = html)
with open("./output/page01.html", "w", encoding="utf-8") as output_file:
    output_file.write(var1)


with open("./input/content/presentation.md", "r", encoding="utf-8") as input_file:
    text_md = input_file.read()
    html = markdown(text_md)
    #print(html)
temp = Environment(loader=FileSystemLoader(searchpath='./')).get_template("template.html")
var2 = temp.render(content = html)

with open("./output/presentation.html", "w", encoding="utf-8") as output_file:
    output_file.write(var2)



with open("./input/content/second-post.md", "r", encoding="utf-8") as input_file:
    text_md = input_file.read()
    html = markdown(text_md)
    #print(html)
temp = Environment(loader=FileSystemLoader(searchpath='./')).get_template("template.html")
var3 = temp.render(content = html)
with open("./output/post02.html", "w", encoding="utf-8") as output_file:
    output_file.write(var3)


venv.create('./output')


