import os

path = r"/Users/jakemeijer/Arts and Facts/" # working directory
for root, dirs, files in os.walk(path):
      for dirss in dirs:
            name = str(dirss.rstrip()) # or strip() to remove space leading and trailing spaces although it might not always work
            os.rename(str(root) + "/" + dirss, str(root) + "/" + name) 
