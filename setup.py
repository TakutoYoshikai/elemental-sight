from setuptools import setup, find_packages

setup(
    name = 'esight',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/elemental-sight.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'This is an extractor of git repository.',
    install_requires = ['setuptools', "GitPython" ],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "esight = esight.esight:main",
        ]
    }
)
