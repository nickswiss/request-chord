import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='request-chord',
    version='0.0.2',
    description='Utility for making a bundle of HTTP requests asynchronously',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    url='https://github.com/nickswiss/request-chord/',
    author='Nick Arnold',
    author_email='nickarnold23@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ]
)
