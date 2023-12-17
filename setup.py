from setuptools import setup
from pkg_resources import parse_requirements
with open('requirements.txt') as root:
    requirements = [str(req) for req in parse_requirements(root)]

setup(
    name='loadmat_v73',
    version='0.0.1',
    packages=['loadmat_v73', 'loadmat_v73.wrapper', 'loadmat_v73.path_tree', 'loadmat_v73.functional'],
    url='',
    license='',
    author='YZ',
    author_email='',
    description='Toolkit to load V7.3 mat file.'
)
