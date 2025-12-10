from setuptools import setup, find_packages,setup


from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path):
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='first_ml_project',
    version='0.1.0',
    author='Subhasis',
    author_email='subhasis1909@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
        