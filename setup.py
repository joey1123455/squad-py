from setuptools import setup

description = (
    'Python API Wrapper for Squadco.com Payment services'
)

setup(
    name='squadco',
    version='1.0.1',
    author='Uche David, Joseph Folayan, Peter Adetunji',
    author_email='debugtitan.hub@outlook.com, folayanjoey@gmail.com, peteradetunji30@gmail.com',
    description=description,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/joey1123455/squad-py.git',
    keywords=['squadco payment gateway','squadco python package', 'squad'],
    packages=['squad'],
    install_requires=['requests'],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 2",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
