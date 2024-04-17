from setuptools import setup, find_packages

setup(
    name='symclone',
    version='0.1.0',
    author='Christoph Hartleb',
    author_email='your@email.com',
    description='A package for symbolic manipulation of DNA sequences',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)