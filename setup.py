import setuptools
from src import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().splitlines()

with open("requirements-dev.txt", "r") as fh:
    extras_require = fh.read().splitlines()

setuptools.setup(
    name="py-rename",
    version=__version__,
    author="Jinal Haria",
    author_email="jinalharia@gmail.com",
    decription="Bulk rename tool for multiple files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jinalharia/py_rename",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    extras_require={
        "dev": extras_require,
    },
    license='MIT',
    python_requires='>=3.6.0',
    entry_points={
        "console_scripts": [
            "py-rename = src:main",
        ],
    },
)