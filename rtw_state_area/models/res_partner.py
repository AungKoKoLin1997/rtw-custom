# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_res_partner_area(models.Model):
    _inherit = 'res.partner'

    rel_region = fields.Char(compute="_get_region", store=True)

    @api.depends('state_id')
    def _get_region(self):
        area1 = ["東京都", "神奈川県", "千葉県", "埼玉県"]
        area2 = ["栃木県", "群馬県", "茨城県"]
        area3 = ["北海道", "青森県", "宮城県", "岩手県", "秋田県", "山形県", "福島県"]
        area4 = ["山梨県", "長野県", "新潟県"]
        area5 = ["静岡県", "三重県", "愛知県", "岐阜県"]
        area6 = ["石川県", "富山県", "福井県"]
        area7 = ["大阪府", "京都府", "滋賀県", "奈良県", "兵庫県", "和歌山県"]
        area8 = ["広島県", "岡山県", "山口県", "島根県", "鳥取県"]
        area9 = ["香川県", "愛媛県", "徳島県", "高知県"]
        area10 = ["福岡県", "大分県", "熊本県", "佐賀県", "長崎県", "宮崎県", "鹿児島県", "沖縄県"]
        for rec in self:
            if rec.state_id.name in area1:
                rec.region = "関東"
            elif rec.state_id.name in area2:
                rec.region = "北関東"
            elif rec.state_id.name in area3:
                rec.region = "東北・北海道"
            elif rec.state_id.name in area4:
                rec.region = "甲信越"
            elif rec.state_id.name in area5:
                rec.region = "東海"
            elif rec.state_id.name in area6:
                rec.region = "北陸"
            elif rec.state_id.name in area7:
                rec.region = "関西"
            elif rec.state_id.name in area8:
                rec.region = "中国"
            elif rec.state_id.name in area9:
                rec.region = "四国"
            elif rec.state_id.name in area10:
                rec.region = "九州・沖縄"
            else:
                rec.region = ""