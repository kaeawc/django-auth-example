#!/usr/bin/env python
from setuptools import setup

version = '1.0'
source = 'https://github.com/kaeawc/django-auth-example'

setup_args = dict(
    name='django-auth-example',
    packages=['django-auth-example'],
    version=version,
    author='Jason Pearson',
    author_email='jason.d.pearson@gmail.com',
    description='Example of Django app with Auth',
    license='MIT',
    keywords='django auth example',
    url=source,
    download_url='%s/archive/%s.zip' % (source, version),
    py_modules=['django-auth-example'],
    tests_require=['pytest'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Toto',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)


if __name__ == '__main__':
    setup(**setup_args)
