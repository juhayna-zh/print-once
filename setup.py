import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="print-once", 
    version="0.0.1",    
    author="Juhayna",   
    author_email="juhayna@foxmail.com", 
    description="Allows you to print certain line only once in the loops.", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juhayna-zh/print-once",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', 
)