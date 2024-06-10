from setuptools import setup, find_packages

eft_version = '2.0.0'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='eft-py',
    version=eft_version,
    description='A python library for easily creating themes for your applications.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Possible Panda',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
    package_data={"eft-py": ["VERSION"]},
)