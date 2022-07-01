#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='LeNet5',
    version='0.0.0',
    description='Implementation of LeNet5',
    author='Max Griffiths',
    author_email='mg13512@bristol.ac.uk',
    url='https://github.com/MaxSkippGriff/MNIST_LeNet5',
    install_requires=[
            'numpy>=1.15.4',
            'torch>=1.0',
            'torchvision>=0.2.1'
    ],
    packages=find_packages(),
)
