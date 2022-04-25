import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="msds",
    version="0.0.2",
    author="Soutick Saha, Chintan Sawla",
    author_email="soutick2010@gmail.com, sawlachintan@gmail.com",
    description="MSDS Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sawlachintan/msds-library",
    project_urls={
        "Bug Tracker": "https://github.com/sawlachintan/msds-library/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        'msds':['*.xlsx']
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
       "pandas==1.2.4",
       "pdfplumber",
       "openpyxl",
   ],
)