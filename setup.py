from distutils.core import setup

setup(
    name='drf-timestamp-pagination',
    version='0.1',
    description='DRF Pagination to work with Timestamp Paginator.',
    packages=['drf_timestamp_pagination', ],
    license='see licence on https://github.com/umutbozkurt/drf-timestamp-pagination',
    long_description='see https://github.com/umutbozkurt/drf-timestamp-pagination/blob/master/README.md',
    url='https://github.com/umutbozkurt/drf-timestamp-pagination',
    download_url='https://github.com/umutbozkurt/drf-timestamp-pagination/releases/',
    keywords=['django', 'timestamp', 'paginator', 'pagination', 'serializer'],
    author='Umut Bozkurt',
    author_email='umutbozkurt92@gmail.com',
    requires=['djangorestframework', 'django_timestamp_paginator'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Text Processing :: Markup :: HTML',
        'Intended Audience :: Developers'
    ],
)
