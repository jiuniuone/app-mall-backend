import datetime

from django.test import TestCase

from mall.models import User, Ads, App, Category, Channel, Device, Host, Cinema, Info, Rom, Video


class BaseTestCase(TestCase):
    DEVICE_MAC_ADDRESS = "48:3b:5A:xC:10:72"
    HOST_MAC_ADDRESS = "10:98:36:A6:AB:55"
    HOST_MAC_ADDRESS2 = "10:98:36:A6:AC:88"

    @classmethod
    def clear(cls):
        User.objects.all().delete()
        Channel.objects.all().delete()
        Cinema.objects.all().delete()
        Device.objects.all().delete()
        Ads.objects.all().delete()
        Rom.objects.all().delete()
        App.objects.all().delete()
        Video.objects.all().delete()
        Category.objects.all().delete()
        Host.objects.all().delete()
        Info.objects.all().delete()

    def setUp(self):
        self.clear()
        self.user=user=User.objects.create(title="aaaa",username="bbbb",password="ccccc")
        self.channel = channel = Channel.objects.create(name="t1xxxx",site_title="",copyright="",description="")
        self.cinema = cinema = Cinema.objects.create(channel=channel, name="cinema1",
                                                  license_due_date=datetime.datetime.strptime('2200-01-01', "%Y-%m-%d"))

        self.host = Host.objects.create(cinema=cinema, name="host1",
                                        mac_address=self.HOST_MAC_ADDRESS,
                                        mac_address2=self.HOST_MAC_ADDRESS2,
                                        ip_address="192.168.1.1", is_primary=True)
        self.device = Device.objects.create(cinema=cinema, mac_address=self.DEVICE_MAC_ADDRESS)
