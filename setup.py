from setuptools import setup, find_packages

setup(
    name = 'git_extract',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/git_extract.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'This is an extractor of git repository.',
    install_requires = ['setuptools', "GitPython" ],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "git-extract = git_extract.git_extract:main",
        ]
    }
)
