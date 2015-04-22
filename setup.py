from distutils.core import setup
setup(
    name = "csudoci",
    packages = ["csudoci", "csudoci.html", "csudoci.ds"],
    version = "0.3.3",
    description = "Libraries for CSUD OCI",
    author = "Cédric Donner",
    author_email = "cedonner@gmail.com",
    url = "https://github.com/oci1315/csudoci",
    download_url = "https://github.com/oci1315/csudoci/releases",
    keywords = ["teaching", "computer science", "Switzerland", "Collège du Sud"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: Development",
        "Environment :: Other Environment",
        "Intended Audience :: Teacher, students",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Teaching :: Libraries :: Python Modules",
        ],
    long_description = """\
This package contains modules and libraries nended for the computer science course
"Option complémentaire informatique" at College du Sud, 1630 Bulle, Switzerland
"""
)
