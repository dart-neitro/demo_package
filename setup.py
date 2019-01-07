from distutils.core import setup

setup(
    name='demo_package1',
    version='0.1.8',
    description='description',

    url='https://github.com/dart-neitro/demo_package1',
    author='Konstantin Neitro',
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # install_requires=['requests'],
    packages=['demo_package', 'demo_package.zzz'],
)
