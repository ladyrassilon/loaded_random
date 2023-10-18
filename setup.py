from setuptools import setup

with open("README.rst") as readme_file:
    long_description = readme_file.read()


DESCRIPTION = """
Given a list of probabilities and outputs at instantiation,
generates random outputs based on the probabilities
"""

setup(
    name="Loaded Random",
    version="0.1",
    packages=[
        "loaded",
    ],
    license="GNU GPL v3.0",
    description=DESCRIPTION,
    author="Gemma Hentsch",
    author_email="contact@halfapenguin.com",
    long_description=long_description,
    keywords=["statistics", "random"],
    test_suite="tests",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
    ],
)
