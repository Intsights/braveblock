import typing


class Adblocker:
    def __init__(
        self,
        rules: typing.List[str],
    ) -> None: ...

    def check_network_urls(
        self,
        url: str,
        source_url: str,
        request_type: str,
    ) -> bool: ...
