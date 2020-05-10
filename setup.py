import os
import sys

import setuptools

import truecase

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "truecase")
sys.path.insert(0, src_dir)


def get_requirements(requirements_path: str = "requirements.txt"):
    with open(requirements_path) as fp:
        return [
            x.strip() for x in fp.read().split("\n") if not x.startswith("#")
        ]


setuptools.setup(
    name="truecase",
    version=truecase.__version__,
    author="Dalton Fury",
    author_email="daltonfury42@disroot.org",
    description="A library to restore capitalization for text",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/daltonfury42/truecase",
    packages=setuptools.find_packages(exclude=["tests"]),
    setup_requires=["pytest-runner"],
    tests_require=get_requirements("requirements.test.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    install_requires=get_requirements(),
    include_package_data=True,
)
