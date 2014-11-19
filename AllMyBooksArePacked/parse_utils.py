from pyquery import PyQuery


def build_query_func(query):
    def qfunc(html):
        d = PyQuery(html)
        return d(query).text()
    return qfunc
