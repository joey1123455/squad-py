from setuptools import setup


description = (
    'Squad API Python '
)

setup(
    name='squadco',
    version='1.0.0',
    author='Uche David <debugtitan.hub@outlook.com>, Joseph Folayan <folayanjoey@gmail.com>, Peter Adetunji <peteradetunji30@gmail.com>',
    author_email='debugtitan.hub@outlook.com',
    description=description,
    long_description="Python Wrapper for Squadco.com Payment services",
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/debugtitan/django-git-storage',
    keywords=['squadco payment gateway','squadco python package', 'squad'],
    packages=['squad'],
    include_package_data=True,
)