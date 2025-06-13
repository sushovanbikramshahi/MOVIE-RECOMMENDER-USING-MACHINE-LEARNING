from setuptools import setup

with open("README.md", "r",encoding="utf_8") as fh:
    long_description=fh.read()

AUTHOR_NAME= 'SUSHOVAN BIKRAM SHAHI'
SRC_REPO= 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='sushovanbikramshahi@gmail.com',
    description='first project',
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)