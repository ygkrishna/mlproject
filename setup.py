from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list of packages from requirements.txt
    '''
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        ## remove \n characters 
        requirements = [req.replace("\n", "") for req in requirements]
        ## remove -e .
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements    

setup(
name = 'mlproject',
version='0.0.1',
author='Gopikrishna',
author_email='gopikrishnayadam@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')




)