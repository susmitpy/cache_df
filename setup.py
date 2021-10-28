from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="cache_df",
    packages=["cache_df"],
    version="0.4",
    license="GPL",
    description="Cache pandas dataframes with a simple interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Susmit Rajeev Vengurlekar",
    author_email="susmit.py@gmail.com",
    url="https://github.com/susmitpy/cache_df",
    download_url="https://github.com/susmitpy/cache_df/archive/refs/tags/v_0.3.tar.gz",
    keywords=["cache pandas dataframe", "cache dataframe", "caching"],
    install_requires=["pandas"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
