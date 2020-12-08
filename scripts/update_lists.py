import requests
import gzip
import pathlib


braveblock_dir = pathlib.Path(__file__).parent.parent.joinpath('braveblock')

easylist_response = requests.get(
    url='https://easylist.to/easylist/easylist.txt',
)
with gzip.GzipFile(
    filename=braveblock_dir.joinpath('easylist.txt.gz'),
    mode='wb',
) as easylist_file:
    easylist_file.write(easylist_response.content)

easyprivacy_response = requests.get(
    url='https://easylist.to/easylist/easyprivacy.txt',
)
with gzip.GzipFile(
    filename=braveblock_dir.joinpath('easyprivacy.txt.gz'),
    mode='wb',
) as easyprivacy_file:
    easyprivacy_file.write(easyprivacy_response.content)
