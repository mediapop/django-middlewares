# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-middlewares',
    version='0.1',
    url='https://github.com/mediapop/django-middlewares',
    author='Hung / Media Pop',
    author_email='hung@mediapop.co',
    description='Django middlewares used for mediapops projects',
    license='BSD',
    long_description=open('README.md').read(),
    packages=find_packages(),
    package_data={
        '': ['README.md']
    },
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)