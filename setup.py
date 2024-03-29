from setuptools import find_packages
from setuptools import setup


version = "1.3.3.dev0"

setup(
    name="recensio.artium",
    version=version,
    description="recensio.artium customizations for Recensio",
    long_description=(open("README.txt").read() + "\n" + open("CHANGES.txt").read()),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python :: 2.7",
    ],
    keywords="web zope plone theme",
    author="Syslab.com GmbH",
    author_email="info@syslab.com",
    url="https://github.com/syslabcom/recensio.artium/",
    license="GPL",
    packages=["vocabularies"] + find_packages(exclude=["ez_setup"]),
    namespace_packages=["recensio"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "recensio.policy",
        "recensio.theme",
        "z3c.jbot",
        "setuptools",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
        ],
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
