from distutils.core import setup

setup(
    name="cache_df",
    packages=["cache_df"],
    version="0.1",
    license="GNU GPLv3",
    description="Cache pandas dataframes with a simple interface",
    author="Susmit Rajeev Vengurlekar",
    author_email="susmit.py@gmail.com",
    url="https://github.com/susmitpy/cache_df",
    download_url="https://github.com/susmitpy/cache_df/archive/v_01.tar.gz",
    keywords=["cache pandas dataframe", "cache dataframe", "caching"],
    install_requires=["pandas"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU GPLv3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
