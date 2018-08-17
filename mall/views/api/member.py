import datetime
import json

import requests

from acmin.utils import attr
from mall.models import Config, Member
from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # https://api.it120.cc/tz/config/get-value?key=mallName
    # http "http://localhost/api/mall/config/get-value?key=mallName"
    fields = "avatar_url,nickname,mobile,id,balance,freeze,score,sign_continuous_days".split(",")

    # http "https://api.it120.cc/tianguoguoxiaopu/user/detail?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route("/member/detail")
    def detail(self):
        member: Member = Member.objects.filter(token=self.param("token")).first()
        if member:
            if (not member.last_sign_date or (datetime.date.today() - member.last_sign_date).days > 1) and member.sign_continuous_days > 0:
                member.sign_continuous_days = 0
                member.save()
            return self.obj_response(member, self.fields)

        return self.file_json_response("/user/detail.json")

    # http "https://api.it120.cc/tianguoguoxiaopu/user/withDraw/apply?token=c6d64df6-50b6-4012-a7e5-868749fe383a&money=100"
    @api_route('/user/withDraw/apply')
    def apply_withdraw(self):
        return self.json_response({"code": 20001, "msg": "可提现余额不足"})

    @api_route('/member/register')
    def register(self):
        code, rawData = self.param(["code", "rawData"])
        open_id, session_key = self.get_session(code)
        if rawData and open_id:
            obj = json.loads(rawData)
            print(obj)
            mmeber: Member = Member.objects.filter(open_id=open_id).first()
            if not mmeber:
                Member.objects.create(
                    open_id=open_id,
                    nickname=obj["nickName"],
                    gender=obj["gender"],
                    language=obj["language"],
                    city=obj["city"],
                    province=obj["province"],
                    country=obj["country"],
                    avatar_url=obj["avatarUrl"],
                    token=""
                )
            return self.json_response({"code": 0})
        return self.json_response({"code": 1})

    def get_session(self, code):
        app_id = Config.objects.filter(name="appId").first().content
        app_secret = Config.objects.filter(name="appSecret").first().content
        url = f"https://api.weixin.qq.com/sns/jscode2session?appid={app_id}&secret={app_secret}&js_code={code}&grant_type=authorization_code"
        json = requests.get(url).json()
        open_id = attr(json, "openid")
        session_key = attr(json, "session_key")
        return open_id, session_key

    # http "http://192.168.31.100/api/mall/user/login?code=033nRnPj2nf00H0EcAPj2l4yPj2nRnPq"
    @api_route('/member/login')
    def login(self):
        open_id, session_key = self.get_session(self.param("code"))
        if open_id and session_key:
            member = Member.objects.filter(open_id=open_id).first()
            if member:
                member.token = session_key
                member.save()
                return self.json_response({"code": 0, "data": {"token": member.token, "uid": member.id}})
            else:
                return self.json_response({"code": 10000})

        return self.json_response({"code": 1, "response": json})

    # http "http://192.168.31.100/api/mall/member/check-token?token=tokenxxxxxxxxxxxxx"
    @api_route('/member/check-token')
    def check_token(self):
        if Member.objects.filter(token=self.param("token")).first():
            return self.json_response({"code": 0})
        return self.json_response({"code": 404})

    # http "https://api.it120.cc/tianguoguoxiaopu/score/sign?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/member/sign')
    def sign(self):
        member = Member.objects.filter(token=self.param("token")).first()
        if member:
            today = datetime.date.today()
            yesterday = today - datetime.timedelta(days=1)
            if not member.last_sign_date or (datetime.date.today() - member.last_sign_date).days > 1:
                member.sign_continuous_days = 1
            else:
                member.sign_continuous_days += 1
            member.save()
            return self.ok()
        return self.error(1, "没有找到对应用户")
