from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='truenorth',

    version='0.1.0',

    description='library for parsing CSV usage history files for Compass Card',
    long_description=long_description,

    url='https://github.com/tdryer/truenorth',

    author='Tom Dryer',
    author_email='tomdryer.com@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='compass card transit csv',

    packages=find_packages(exclude=['tests']),

    install_requires=[],

    extras_require={
        'test': ['pytest'],
    },

    entry_points={
        'console_scripts': [
            'truenorth=truenorth.__main__:main',
        ],
    },
)
