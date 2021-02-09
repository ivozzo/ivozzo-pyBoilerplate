import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ivozzo-pyboilerplate",
    version="1.0.0",
    author="ivozzo",
    description="Python boilerplate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" https://github.com/ivozzo/ivozzo-pyBoilerplate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)