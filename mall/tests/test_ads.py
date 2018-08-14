from .base import *


class Case(BaseTestCase):
    def setUp(self):
        super().setUp()

        Ads.objects.create(
            hotel=self.hotel,
            ads_position=1,
            duration=10,
            title="title1",
            ads_type=2,
            url="http://xx.cn/static/hotel_pic.png",
            detail_url="http://xx.cn/static/hotel_pic.png",
        )

    def test_has_data(self):
        orignal = self.DEVICE_MAC_ADDRESS
        for mac in [orignal.lower(), orignal.upper(), orignal.capitalize(), orignal.swapcase()]:
            response = self.client.get("/api/hotel/ads/?position=1&imei=%s" % mac)
            self.assertEqual(200, response.status_code)
            json = response.json()
            self.assertEqual(0, json["status"])
            self.assertEqual(1, len(json["data"]))

    def test_no_data(self):
        response = self.client.get("/api/hotel/ads/?position=4&imei=%s" % self.DEVICE_MAC_ADDRESS)
        self.assertEqual(200, response.status_code)
        json = response.json()
        self.assertEqual(0, json["status"])
        self.assertEqual(0, len(json["data"]))

    def test_invalid_param(self):
        response = self.client.get("/api/hotel/ads/?position=4")
        self.assertEqual(200, response.status_code)
        json = response.json()
        self.assertEqual(1, json["status"])
        self.assertFalse("data" in json)
        message = 'invalid params'
        self.assertEqual(message, json["message"])
