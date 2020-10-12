import unittest

import braveblock


class BraveblockTestCase(
    unittest.TestCase,
):
    def test_adblocker_default_rules(
        self,
    ):
        adblocker = braveblock.Adblocker()

        self.assertFalse(
            expr=adblocker.check_network_urls(
                url='http://some-website.com/image.jpg',
                source_url='http://some-website.com/',
                request_type='image',
            ),
        )
        self.assertTrue(
            expr=adblocker.check_network_urls(
                url='http://some-google-ads.com/image.jpg',
                source_url='http://some-google-ads.com/',
                request_type='image',
            ),
        )
        self.assertTrue(
            expr=adblocker.check_network_urls(
                url='http://some-google-analytics.com/image.jpg',
                source_url='http://some-google-analytics.com/',
                request_type='image',
            ),
        )

    def test_adblocker_custom_rules(
        self,
    ):
        adblocker = braveblock.Adblocker(
            rules=[
                '-advertisement-icon.',
            ],
            include_easylist=False,
            include_easyprivacy=False,
        )

        self.assertTrue(
            expr=adblocker.check_network_urls(
                url='http://domain.com/some-advertisement-icon.',
                source_url='http://domain.com/',
                request_type='image',
            ),
        )
        self.assertFalse(
            expr=adblocker.check_network_urls(
                url='http://domain.com/other-icon.ico',
                source_url='http://domain.com/',
                request_type='image',
            ),
        )

        self.assertFalse(
            expr=adblocker.check_network_urls(
                url='http://some-website.com/image.jpg',
                source_url='http://some-website.com/',
                request_type='image',
            ),
        )

        self.assertFalse(
            expr=adblocker.check_network_urls(
                url='http://google-ads.com/image.jpg',
                source_url='http://google-ads.com/',
                request_type='image',
            ),
        )
        self.assertFalse(
            expr=adblocker.check_network_urls(
                url='http://some-google-analytics.com/image.jpg',
                source_url='http://some-google-analytics.com/',
                request_type='image',
            ),
        )

    def test_adblocker_custom_rules_plus_default(
        self,
    ):
        adblocker = braveblock.Adblocker(
            rules=[
                '-advertisement-icon.',
            ],
        )

        self.assertTrue(
            expr=adblocker.check_network_urls(
                url='http://legitimate.com/some-advertisement-icon.',
                source_url='http://legitimate.com/',
                request_type='image',
            ),
        )
        self.assertFalse(
            expr=adblocker.check_network_urls(
                url='http://legitimate.com/other-icon.ico',
                source_url='http://legitimate.com/',
                request_type='image',
            ),
        )

        self.assertFalse(
            expr=adblocker.check_network_urls(
                url='http://legitimate.com/image.jpg',
                source_url='http://legitimate.com/',
                request_type='image',
            ),
        )

        self.assertTrue(
            expr=adblocker.check_network_urls(
                url='http://google-ads.com/image.jpg',
                source_url='http://google-ads.com/',
                request_type='image',
            ),
        )
        self.assertTrue(
            expr=adblocker.check_network_urls(
                url='http://some-google-analytics.com/image.jpg',
                source_url='http://some-google-analytics.com/',
                request_type='image',
            ),
        )
