import typing


class Adblocker:
    def __init__(
        self,
        rules: typing.Optional[typing.List[str]] = None,
        include_easylist: bool = True,
        include_easyprivacy: bool = True,
    ) -> None: ...

    def check_network_urls(
        self,
        url: str,
        source_url: str,
        request_type: str,
    ) -> bool: ...
