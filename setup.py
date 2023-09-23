from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path: str)->List[str]:
    '''
    Returns a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
    return requirements    


setup(
name='mlproject1',
version='1.0.0',
author='san',
author_email='san@mlproject.org',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
    
)

