import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="truecase",
    version="0.0.4",
    author="Dalton Fury",
    author_email="daltonfury42@disroot.org",
    description="A library to restore capitalization for text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daltonfury42/truecase",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['nltk'],
    include_package_data=True
)
