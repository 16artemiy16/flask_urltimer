"""
flask_urltimer
--------------

Flask extension to measure endpoints timings.
"""

from setuptools import setup

setup(
    name='flask_urltimer',
    version='1.0',
    author='Artem Polikarpov',
    author_email='artemiypolikarpov@gmail.com',
    description='Flask extension to measure endpoints timings.',
    long_description=__doc__,
    include_package_data=True,
    platforms='any',
    packages=['flask_urltimer'],
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
