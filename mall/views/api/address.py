from mall.models import Address, City, District, Member, Province
from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # http "https://api.it120.cc/tianguoguoxiaopu/address/list?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/address/list')
    def list(self):
        member: Member = Member.objects.filter(token=self.param("token")).first()
        if member:
            addresses = Address.objects.filter(member=member).all()
            if addresses:
                return self.json_response({"code": 0, "data": [a.to_json() for a in addresses]})
        return self.json_response({"code": 700, "msg": "暂无数据"})

    # http "https://api.it120.cc/tianguoguoxiaopu/address/update?token=c6d64df6-50b6-4012-a7e5-868749fe383a&id=31730&isDefault=true"
    @api_route('/address/update')
    def update(self):
        address = self.compose_address()
        if address:
            address = Address.objects.filter(mem).first()
            if address:
                return self.json_response({"code": 0, "data": address.to_json()})

        return self.json_response({"code": 700, "msg": "暂无数据"})

    # http "http://localhost/api/mall/address/default?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/address/default')
    def default(self):
        member: Member = Member.objects.filter(token=self.param("token")).first()
        if member:
            address = Address.objects.filter(member=member).order_by("-is_default").first()
            print(address.id)
            if address:
                return self.json_response({"code": 0, "data": address.to_json()})
        return self.file_json_response("/address/default.json")

    def compose_address(self):
        token, address, mobile, addressee = self.param(["token", "address", "mobile", "addressee"])
        province_id = self.int_param('provinceId')
        city_id = self.int_param('cityId')
        district_id = self.int_param('districtId')
        code = self.int_param('code')
        is_default = self.param("isDefault") == 'true'
        provice = Province.objects.filter(id=province_id).first()
        city = City.objects.filter(id=city_id).first()
        district = District.objects.filter(id=district_id).first()
        member: Member = Member.objects.filter(token=token).first()
        id = self.int_param("id", 0)
        if id == 0: id = None
        if member and provice and city:
            return Address(
                id=id,
                member=member,
                provice=provice,
                city=city,
                district=district,
                address=address,
                code=code,
                addressee=addressee,
                phone_number=mobile,
                is_default=is_default
            )

    # http "https://api.it120.cc/tianguoguoxiaopu/address/add?token=c6d64df6-50b6-4012-a7e5-868749fe383a&id=0&provinceId=320000&cityId=320400&districtId=320401&linkMan=%E6%9F%90%E6%9F%90%E6%9F%90&address=%E5%97%AF%E5%97%AF&mobile=13522222222&code=132466&isDefault=true"
    @api_route('/address/add')
    def add(self):
        address = self.compose_address()
        if address:
            address.save()
            return self.json_response({"code": 0, "data": address.to_json()})

        return self.json_response({"code": 700, "msg": "创建失败"})

    # http "https://api.it120.cc/tianguoguoxiaopu/address/detail?token=c6d64df6-50b6-4012-a7e5-868749fe383a&id=31730"
    @api_route('/address/detail')
    def detail(self):
        id = self.int_param("id")
        address = Address.objects.filter(id=id).first()
        if address:
            return self.json_response({"code": 0, "data": address.to_json()})

        return self.json_response({"code": 700, "msg": "暂无数据"})

    @api_route('/address/delete')
    def delete(self):
        address = Address.objects.filter(id=self.int_param("id"))
        if address:
            address.delete()
            return self.json_response({"code": 0, "msg": "success"})

        return self.json_response({"code": 700, "msg": "删除失败"})
