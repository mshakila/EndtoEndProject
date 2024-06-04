
from setuptools import find_packages , setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str)->List(str):
    requirements = []
    with open(file_path) as file_obj:   # opens requirements file
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] # keeps all requirements inside list

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup(
    name = "DiamondPricePrediction",
    version = "0.0.1", 
    author = "binte Sajida Khanum",
    author_email = "xxxxxx@gmail.com",
    #install_requires = ["scikit-learn","pandas", "numpy"] # here doing manually
    install_requirements = get_requirements("requirements.txt") # here, we are getting requirements , this is automated
    packages = find_packages()
)