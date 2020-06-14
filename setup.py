from setuptools import setup, find_packages

try:
    readme = open("README.md")
    long_description = str(readme.read())
finally:
    readme.close()

setup(
    name="LifeHub",
    version="0.0",
    packages=find_packages(),
    long_description=long_description,
    install_requires=["pygame"],
    package_data={
        "LifeHub": ["en/LC_MESSAGES/*.mo", "pl/LC_MESSAGES/*.mo"],
    },
    # metadata to display on PyPI
    author="Владимир Шапошников, Владимир Рябченков, Андрей Морквин",
    description="This is LifeHub package",
    url="https://github.com/Matavilla/LifeHub",  # project home page, if any
)
