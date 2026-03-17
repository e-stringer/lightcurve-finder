from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as f:
    readme = f.read()+"\n\n"
scripts = ['lightcurve-finder']
setup(
    name="lightcurve-finder",
    version="0.1.0",
    include_package_data=True,
    python_requires='>=3.10.13',
    packages=find_packages(),
    install_requires=requirements,
    scripts=scripts,
    author="Eric Stringer",
    author_email="ericpstringer@yahoo.com",
    description="A tool to query lightcurves from ZTF, Gaia, ASAS-SN, and TESS",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.10.13",
        "License :: OSI Approved :: BSD-3-Clause",
        "Operating System :: OS Independent",
    ],
)
