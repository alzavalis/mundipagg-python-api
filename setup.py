from setuptools import setup

setup(name='mundipagg-python-api',
      version='1.0',
      description="Mundipagg API",
      long_description="",
      author='Andre Galdino',
      author_email='agaldino@mundipagg.com',
      license='Apache License v2.0',
      packages=['mundipagg'],
      zip_safe=False,
      install_requires=[
          'suds',
          ],
      )