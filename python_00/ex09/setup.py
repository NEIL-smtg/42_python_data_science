from setuptools import setup, find_packages

"""
    python setup.py sdist bdist_wheel

    sdist - build tar.gz file (source distribution package),
    contains complete source code and any
    neccesssary file that required to build the package

    bdist_wheel -  build .whl file, more efficient and faster
    contain precompile code, preferred for prebuilt package
"""

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    url='#',
    author='suchua',
    author_email='sunghui2000@gmail.com',
    license='MIT',
    packages=find_packages(),
    classifiers='',
)
