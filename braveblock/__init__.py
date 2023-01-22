import gzip
import sys
import importlib.resources
import typing

from . import braveblock

PY_VERSION_MAJOR = sys.version_info.major
PY_VERSION_MINOR = sys.version_info.minor


class Adblocker:

    @staticmethod
    def read_gz_binary(
        file_name: str
    ) -> bytes:
        if PY_VERSION_MAJOR < 3 or PY_VERSION_MINOR < 11:
            return importlib.resources.read_binary(
                package=__package__,
                resource=file_name,
            )
        with importlib.resources.files(
            __package__,
        ).joinpath(
            file_name,
        ).open(
            'rb',
        ) as _word_frequencies_binary:
            return _word_frequencies_binary.read()

    def __init__(
        self,
        rules: typing.Optional[typing.List[str]] = None,
        include_easylist: bool = True,
        include_easyprivacy: bool = True,
    ) -> None:
        combined_rules = []

        if rules is not None:
            combined_rules.extend(
                rules
                )

        if include_easylist:
            easylist_compressed_data = self.read_gz_binary(
                file_name='easylist.txt.gz',
            )
            easylist_data = gzip.decompress(
                easylist_compressed_data
                ).decode()
            easylist_rules = easylist_data.splitlines()
            combined_rules.extend(
                easylist_rules
                )

        if include_easyprivacy:
            easyprivacy_compressed_data = self.read_gz_binary(
                file_name='easyprivacy.txt.gz',
            )

            easyprivacy_data = gzip.decompress(
                easyprivacy_compressed_data
                ).decode()
            easyprivacy_rules = easyprivacy_data.splitlines()
            combined_rules.extend(
                easyprivacy_rules
                )

        self.engine = braveblock.Adblocker(
            rules=combined_rules,
        )

    def check_network_urls(
        self,
        url: str,
        source_url: str,
        request_type: str,
    ) -> bool:
        return self.engine.check_network_urls(
            url=url,
            source_url=source_url,
            request_type=request_type,
        )
