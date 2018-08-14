from mall.views.api import ApiView, api_route


class Resource(ApiView):
    # https://api.it120.cc/tz/config/get-value?key=mallName
    # http "http://localhost/api/mall/config/get-value?key=mallName"
    @api_route('/config/get-value')
    def get_value(self):
        key = self.param("key")
        if key == 'mallName':  return self.file_json_response("/config/get-value/mallName.json")
        if key == 'recharge_amount_min': return self.file_json_response("/config/get-value/recharge_amount_min.json")
        if key == 'shopPrompt': return self.file_json_response("/config/get-value/shopPrompt.json")
        if key == 'shopDelivery':  return self.file_json_response("/config/get-value/shopDelivery.json")
        if key == 'shopDeliveryPrice': return self.file_json_response("/config/get-value/shopDeliveryPrice.json")
        if key == 'couponsTitlePicStr':  return self.file_json_response("/config/get-value/couponsTitlePicStr.json")
        if key == 'aboutUsTitle': return self.file_json_response("/config/get-value/aboutUsTitle.json")
        if key == 'servicePhoneNumber': return self.file_json_response("/config/get-value/servicePhoneNumber.json")
        if key == 'aboutUsContent': return self.file_json_response("/config/get-value/aboutUsContent.json")
        if key == 'finderRecommendTtile': return self.file_json_response("/config/get-value/finderRecommendTtile.json")
        return self.json_response({})
