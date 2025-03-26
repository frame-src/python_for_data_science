from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

setup(
        name="ft_package", 
        version=VERSION,
        author="frame-src",
        author_email="frame-src@MAIL.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'first package'],
        classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        ],
)

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    author='eagle',
    author_email='eagle@42.fr',
    url='https://github.com/eagle/ft_package',
    license='MIT',
    packages=find_packages(),
    
    python_requires='>=3.6',
)