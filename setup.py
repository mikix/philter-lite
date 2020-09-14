import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="philter-lite",
    version="2.0.0",
    author="Beau Norgeot",
    author_email="beaunorgeot@gmail.com",
    description="An open-source PHI-filtering software",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BCHSI/philter-ucsf",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["philter_lite = philter_lite.main:main",],},
    install_requires=["chardet~=3.0", "nltk~=3.5", "xmltodict~=0.12",],
)
