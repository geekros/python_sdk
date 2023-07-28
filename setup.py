from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="robotchain",
    version="1.0.0",
    author="MakerYang",
    author_email="admin@wileho.com",
    description="Python development framework for robotchain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geekros/python_framework_sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7.5",
)
