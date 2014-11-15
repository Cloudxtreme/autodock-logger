#!/usr/bin/env python


from setuptools import setup


setup(
    name="autodock-logger",
    version="0.0.1",
    description="autodock logger plugin",
    install_requires=[],
    # XXX: Use upstream dependencies
    # install_requires=[
    #     "autodock",
    #     "circuits"
    # ],
    scripts=["autodock-logger"]
)
