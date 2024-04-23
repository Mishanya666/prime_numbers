from setuptools import setup, find_packages

setup(
    name='my_prime_numbers_project',
    version='1.0',
    description='Project that finds prime numbers',
    long_description_content_type='text/markdown',
    license='MIT',
    author='Mishanya666',
    author_email='dacko7541@gmail.com',
    url='https://github.com/standlab/mtracker',
    packages=find_packages(),
    install_requires=[],  # it is empty since we use standard python library
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
    python_requires='>=3',
)
