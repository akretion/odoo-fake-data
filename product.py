#!/usr/bin/env python
# coding: utf-8
##############################################################################
#
#    Author: David BEAL
#    Copyright 2015 Akretion
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from .common import *

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def insert_prd(categ_ids=[1]):
    Product = client.model('product.product')
    couleur = random.choice(cf.COLORS)
    name = '%s %s ' % (random.randint(1, 1000), couleur)
    vals = {
        'profile_id': 1,
        'name': name + "bla bla designation",
        'categ_id': random.choice(categ_ids),
        'list_price': random.randint(1, 100),
        'default_code': '%s-%sM' % (
            random.randint(1, 958), random.choice(
                cf.PRODUCT_CODE_SUBSET_FAKE)),
    }
    if cf.CREATE_IMG:
        x = random.randint(500, 1000)
        y = random.randint(500, 1000)
        im = Image.new('RGBA', (x, y), couleur)
        font = ImageFont.truetype(cf.FONT, 70)
        draw = ImageDraw.Draw(im)
        draw.text((0, (x+y)/5-2),  unicode(name, 'UTF-8'), font=font)
        del draw
        b = io.BytesIO()
        im.save(b, cf.IMG_FORMAT)
        tmp = b.getvalue()
        image_base64 = base64.b64encode(tmp)
        vals['image'] = image_base64
    Product.create(vals)
    return True


def get_product_category():
    Categ = client.model('product.category')
    return Categ.self.search([])


if __name__ == '__main__':
    categ_ids = get_product_category()
    for i in range(1, 80):
        insert_prd(categ_ids)
