#from pyquery import PyQuery

from parse_utils import build_query_func


things_to_pull = {
    "title": build_query_func("#btAsinTitle"),
    "author": build_query_func("div.buying > span > a"),
    "price":  build_query_func("b.priceLarge"),
    "shipping_weight": build_query_func("#productDetailsTable li:contains('Shipping Weight')"),
    "isbn-10": build_query_func("#productDetailsTable li:contains('ISBN-10')"),  # seems to be a bug in the contains implementation
}
