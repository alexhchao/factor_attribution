import setuptools

#with open("README.md", "r") as fh:
#    long_description = fh.read()

setuptools.setup(
    name="factorAttribution",
    version="0.0.1",
    author="Alex Chao",
    author_email="alexchao86@gmail.com",
    description="A small example package",
    long_description="factor risk and return attributions",
    long_description_content_type="text/markdown",
    url="https://github.com/alexhchao/factor_attribution",
    packages=setuptools.find_packages(),
)

