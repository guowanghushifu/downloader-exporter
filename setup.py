from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='downloader-exporter',
    packages=['downloader_exporter'],
    version='0.5.2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Prometheus exporter for torrent downloader like qbittorrent/transmission/deluge',
    author='Lei Shi',
    author_email='me@leishi.io',
    url='https://github.com/guowanghushifu/downloader-exporter',
    download_url='https://github.com/guowanghushifu/downloader-exporter/archive/0.5.2.tar.gz',
    keywords=['prometheus', 'qbittorrent', 'transmission', 'deluge'],
    classifiers=[],
    python_requires='>=3.6.2',
    install_requires=[
        'attrdict==2.0.1',
        'deluge-client==1.10.2',
        'loguru==0.7.2',
        'qbittorrent-api==2024.5.63',
        'transmission-rpc==7.0.10',
        'prometheus_client==0.20.0',
        'pyyaml==6.0.1',
    ],
    entry_points={
        'console_scripts': [
            'downloader-exporter=downloader_exporter.exporter:main',
        ]
    }
)
