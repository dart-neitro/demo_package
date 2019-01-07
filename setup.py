from setuptools import setup, find_packages
import os

here = os.path.dirname(os.path.abspath(__file__))

requirements_file = os.path.join(here, 'requirements.txt')
if os.path.exists(requirements_file) and os.path.isfile(requirements_file):
    with open(requirements_file) as f:
        install_requires = [
            x.strip() for x in f.read().split('\n') if x.strip()]
else:
    install_requires = []

setup(
    name='demo_package',
    version='0.1.14',
    description='description :: (%s) (%s) ' % (
        requirements_file, os.listdir(here)),

    url='https://github.com/dart-neitro/demo_package',
    author='Konstantin Neitro',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=install_requires,
    # packages=['demo_package', 'demo_package.zzz'],
)
