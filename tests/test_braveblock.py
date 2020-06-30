import unittest

import braveblock


class BraveblockTestCase(
    unittest.TestCase,
):
    def test_adblocker(
        self,
    ):
        adblocker = braveblock.Adblocker(
            rules=[
                '-advertisement-icon.',
            ],
        )

        self.assertTrue(
            expr=adblocker.check_network_urls(
                url='http://domain.com/-advertisement-icon.',
                source_url='',
                request_type='image',
            ),
        )
        self.assertFalse(
            expr=adblocker.check_network_urls(
                url='http://domain.com/other-icon.ico',
                source_url='',
                request_type='image',
            ),
        )
