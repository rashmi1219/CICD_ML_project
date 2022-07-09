from setuptools import setup
from typing import List

#declaring variables for setup function
PROJECT_NAME="housing_predictor"
VERSION="0.0.1"
AUTHOR="rashmi"
DESCRIPTION="this is the first ml project"
PACKAGES=["housing"] #this has to be in list form
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description:this function is going to return list of requirement mentioned in 
    requirements.txt file 

    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()

)
