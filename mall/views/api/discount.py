import datetime

from mall.models import Coupon, Member, MemberCoupon
from mall.views.api import ApiView, api_route


class Resource(ApiView):
    output_fields = "id,name,threshold,reduce,total,expiry_date,end_date".split(",")

    # http "https://api.it120.cc/tianguoguoxiaopu/discounts/my?token=c6d64df6-50b6-4012-a7e5-868749fe383a&status=0"
    @api_route('/discounts/my')
    def my(self):
        member: Member = Member.objects.filter(token=self.param("token")).first()
        if member:
            today = datetime.date.today()
            coupons = [mc.coupon for mc in MemberCoupon.objects.filter(
                member=member, coupon__start_date__lte=today, coupon__end_date__gte=today
            ).all()]
            return self.list_response(coupons, self.output_fields)
        return self.error(700, "no data")

    # http "https://api.it120.cc/tianguoguoxiaopu/discounts/coupons?type="
    @api_route('/discounts/coupons')
    def coupons(self):
        today = datetime.date.today()
        return self.list_response(
            Coupon.objects.filter(start_date__lte=today, end_date__gte=today).all(),
            self.output_fields
        )

    # 领优惠券
    # http "https://api.it120.cc/tianguoguoxiaopu/discounts/fetch?id=864&token=c6d64df6-50b6-4012-a7e5-868749fe383a"
    @api_route('/discounts/fetch')
    def fetch(self):
        member: Member = Member.objects.filter(token=self.param("token")).first()
        coupon: Coupon = Coupon.objects.filter(pk=self.int_param("id")).first()
        if member and coupon:
            MemberCoupon.objects.create(member=member, coupon=coupon)
            coupon.left = coupon.left - 1
            coupon.save()
            return self.obj_response(coupon, self.output_fields)

        return self.error(1, "获取失败")
