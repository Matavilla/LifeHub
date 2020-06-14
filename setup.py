from setuptools import setup, find_packages


setup(
    name="LifeHub",
    version="0.0",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["pygame"],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.rst", "*.md"],
    },

    # metadata to display on PyPI
    author="Владимир Шапошников, Владимир Рябченков, Андрей Морквин",
    #author_email="me@example.com",
    description="This is LifeHub package",
    url="https://github.com/Matavilla/LifeHub",  # project home page, if any
    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },
    # classifiers=[
    #     "License :: OSI Approved :: Python Software Foundation License"
    # ]

    # could also include long_description, download_url, etc.
)
