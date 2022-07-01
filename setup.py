#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='LeNet5',
    version='0.0.0',
    description='Implementation of LeNet5',
    author='Max Griffiths',
    author_email='mg13512@bristol.ac.uk',
    url='https://github.com/MaxSkippGriff/MNIST_LeNet5',
    install_requires=['pytorch-lightning'],
    packages=find_packages(),
)
