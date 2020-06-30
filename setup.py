import setuptools
import setuptools_rust


setuptools.setup(
    name='braveblock',
    version='0.1.0',
    author='Gal Ben David',
    author_email='gal@intsights.com',
    url='https://github.com/intsights/braveblock',
    project_urls={
        'Source': 'https://github.com/intsights/braveblock',
    },
    license='MIT',
    description='A fast and easy adblockplus parser and matcher based on adblock-rust package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='adblock ads adblocker rust brave abp',
    python_requires='>=3.6',
    zip_safe=False,
    rust_extensions=[
        setuptools_rust.RustExtension(
            target='braveblock.braveblock',
        ),
    ],
    setup_requires=[
        'setuptools-rust',
        'wheel',
    ],
    install_requires=[],
    tests_require=[
        'gitpython',
    ],
    packages=[
        'braveblock',
    ],
    package_data={},
    include_package_data=True,
)
