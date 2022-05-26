#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()


setup(
    name="adaptor",
    version='0.1.4',
    description="Adaptor: Objective-centric Adaptation Framework for Language Models.",
    long_description_content_type="text/markdown",
    long_description=readme,
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3.8"
    ],
    author="Michal Stefanik",
    author_email="stefanik.m@mail.muni.cz",
    url="https://github.com/gaussalgo/adaptor",
    python_requires=">=3.7",
    license="MIT",
    packages=find_packages(include=["adaptor", "adaptor.*"]),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "torch>=1.7",
        "transformers==4.19.1",
        "sentencepiece",
    ],
    test_require=[
        "pytest"
    ],
    extras_require={
        "generative": [
            "sacrebleu",
            "rouge-score",
            "bert-score",
            "fairseq",
            "protobuf",
        ],
        "examples": [
            "comet-ml",
        ],
    },
)
