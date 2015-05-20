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


import erppeek
import io
import random
import base64


try:
    from . import config as cf
except:
    from . import config_fake as cf

try:
    from . import credential as cred
except:
    from . import credential_fake as cred

client = erppeek.Client(cred.URL + cred.PORT, cred.DATABASE,
                        cred.USER, cred.PASSWORD)
