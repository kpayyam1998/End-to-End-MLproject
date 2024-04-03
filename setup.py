from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ." # if it doesnt want to read

def get_requirements(file_path:str)->List[str]:

    '''
        This function will return the list of the components
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # this line read and return \n so wee need to remove it
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="End_to_End_ML",
    version="0.0.1",
    author="kps",
    author_email="kps@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)