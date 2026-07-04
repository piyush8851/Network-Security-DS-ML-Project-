from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    '''
    This function return list of requirements from requirements.txt file
    '''
    requirements_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #Read Lines from file
            lines = file.readlines()

            ##Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty line and last line (-e .)
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirements_lst

print(get_requirements)

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Piyush Chaudhary',
    author_email='piyushchaudhary6397@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)
