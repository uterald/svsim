from distutils.core import setup

files=["reads/*","data/*"]

setup(
    name="svsim",
    version="0.1dev",
    license="Modified BSD",
    packages=["svsim"],
    package_data={"svsim":files},
    long_description = open( "README.md", "r" ).read( ),
    url="http://www.example.com/",
    maintainer="The svest team.",
    maintainer_email="mattias.franberg@scilifelab.se"
)
