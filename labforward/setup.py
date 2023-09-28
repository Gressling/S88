from setuptools import setup, find_packages

setup(
    name="labforward-api-library",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "http.client",
        "urllib.parse",
        "base64",
        "json",
        "xml.etree.ElementTree",
        "xml.dom.minidom",
        "pandas",
        "python-dotenv",
    ],
    author="Peter Dinh & Alexander Reiling",
    author_email="peter.dinh@bayer.com",
    description="A Python library for interacting with LabForward APIs and creating a XML or dataframe from Laboperator at Bayer",
    url="https://github.com/Gressling/S88-light/tree/main/labforward",
)
