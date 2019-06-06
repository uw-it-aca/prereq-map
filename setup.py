import os
from setuptools import setup

README = """
See the README on `GitHub
<https://github.com/uw-it-aca/prereq_map>`_.
"""

# The VERSION file is created by travis-ci, based on the tag name
version_path = 'prereq_map/VERSION'
print(os.path.join(os.path.dirname(__file__), version_path))
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

url = "https://github.com/uw-it-aca/prereq_map"
setup(
    name='Prerequisite Map',
    version=VERSION,
    packages=['prereq_map'],
    author="UW-IT AXDD",
    author_email="aca-it@uw.edu",
    include_package_data=True,
    install_requires=[
        'django>=2.1,<2.2',
        'django-webpack-loader',
        'pandas',
        'inflector',
        'UW-RestClients-SWS>=2.1,<3.0'
    ],
    license='Apache License, Version 2.0',
    description='A tool for visually displaying UW course prerequisites',
    long_description=README,
    url=url,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
