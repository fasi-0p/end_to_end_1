import os
from pathlib import Path
import logging

project_name="datascience"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", #so entire folder can be converted to package to be imported later
    f"src/{project_name}/components/__init__.py", #components=pipeline for preprocessing and also to be imported
    f"src/{project_name}/utils/__init__.py", #generic functions to be packages and imported
    f"src/{project_name}/utils/common.py", #generic functions where it exists
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",#will have training and prediction pipeline
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html"
]

for file in list_of_files:
    filedir,filename=os.path.split(file)
    if(filedir!=""):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"directory {filename} created")
    
    if(not os.path.exists(filename)) or (os.path.getsize(filename)==0): #no idea wtf this part is
        with open(filename,"w") as f:
            pass
            logging.info(f"file {filename} created")
    else:
        logging.info(f"file {filename} already exists")