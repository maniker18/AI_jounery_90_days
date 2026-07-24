import os
from pathlib import Path
 
# the differ between os and pathlib is os uses string path uses object

# print(Path.cwd())

# gives all the items in given cwd
# for p in Path().iterdir():
#     print(p)


# my_dir = Path("api key")
# pyt = Path("project")

# newfile =my_dir/"prompts/sys_ins.txt"
# # it is used for joining new files or project

# print(my_dir)
# # print(pyt.exists())
# print(newfile.exists())

#  .parent gives directory of parent
# differ btw resolve and aboslute is both gives absoutle path but resolve is used to 
# avoid slim and reltaives so we mainly use resolve
# print(my_dir.parent.absolute().parent.parent)
# print(my_dir.parent.resolve().parent.parent)

# p =Path("..").absolute() it adds the .. but actually means parents class so we 
# resolve p =Path("..").resolve()
# bes t way to accces curent file and to parent is 
# p =Path(__file__).resolve().parent

# p =Path.home()/"Desktop"/"AI-Agent"/"a"/"New Text Document.txt"

# # for a in p.rglob("*txt*",case_sensitive=False):
# #     print(a)
 
# with open(p) as f:
#    print(f.read())


# for making dir 
# p = Path("temo")
# p.mkdir()

# # for making  file 
# f = Path("file.txt")
# f.touch()

# we should use replace instead of rename beacuse itmay give error
#  in other os 
# print(Path.ANTHROPIC_API_KEY())

from pathlib import Path
p = Path.cwd()
files = p.rglob('*.py')
for f in files:
    print(f)

