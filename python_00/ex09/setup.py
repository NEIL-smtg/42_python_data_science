from setuptools import setup, find_packages

"""
    python setup.py sdist bdist_wheel
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
    include_dirs='',
    zip_safe=False,
    long_description="README.md",
)
