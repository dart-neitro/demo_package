from setuptools import setup, find_packages

setup(
    name='demo_package',
    version='0.1.9',
    description='description',

    url='https://github.com/dart-neitro/demo_package1',
    author='Konstantin Neitro',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # install_requires=['requests'],
    # packages=['demo_package', 'demo_package.zzz'],
)
