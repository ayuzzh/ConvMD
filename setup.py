from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Tool for converting Markdown into HTML'

setup(
        name="convmd",
        version=VERSION,
        author="Ayush K M",
        author_email="kmayushkm@gmail.com",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=["pygments"],
	license="GPL-3.0",
	url="https://github.com/ayuzzh/ConvMD",
	keywords=['python', 'markdown', 'html'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
