import base64
import json

import requests
from Crypto.Cipher import AES

from acmin.utils import attr
from mall.models import Member
from mall.views.api import ApiView, api_route


class WXBizDataCrypt:
    def __init__(self, appId, sessionKey):
        self.appId = appId
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)
        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))
        if decrypted['watermark']['appid'] != self.appId:
            raise Exception('Invalid Buffer')
        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]


class Resource(ApiView):
    # https://api.it120.cc/tz/config/get-value?key=mallName
    # http "http://localhost/api/mall/config/get-value?key=mallName"

    # http "https://api.it120.cc/tianguoguoxiaopu/user/amount?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/user/amount')
    def amount(self):
        return self.json_response({"code": 0, "data": {"balance": 0.00, "freeze": 0.00, "score": 50, "totleConsumed": 0.00}, "msg": "success"})

    # http "https://api.it120.cc/tianguoguoxiaopu/user/detail?token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route("/user/detail")
    def detail(self):
        return self.file_json_response("/user/detail.json")

    # http "https://api.it120.cc/tianguoguoxiaopu/user/withDraw/apply?token=c6d64df6-50b6-4012-a7e5-868749fe383a&money=100"
    @api_route('/user/withDraw/apply')
    def apply_withdraw(self):
        return self.json_response({"code": 20001, "msg": "可提现余额不足"})

    @api_route('/member/register')
    def register(self):
        app_id = 'wx775c8bd3c7c0d5df'
        code, userInfo, iv = self.param(["code", "userInfo", "iv"])
        open_id, session_key = self.get_session(code)
        print(code, userInfo, iv)
        pc = WXBizDataCrypt(app_id, session_key)
        print(pc.decrypt(userInfo, iv))
        return self.json_response({"code": 1, })

    def get_session(self, code):
        app_id = 'wx775c8bd3c7c0d5df'
        app_secret = '7922df1b3a46fb0e189460740d8c281f'
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
