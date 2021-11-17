from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'avlib'
LONG_DESCRIPTION = 'Libary zum erstellen eines Arbeitsvertrages. Benötigt TeXlive installation.'

setup(
        name="avlib", 
        version=VERSION,
        author="Artem Biryukov",
        author_email="leck@mich",
        scripts=[],
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        url="",
        
        keywords=['python'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX",
        ]
)
