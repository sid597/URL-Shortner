# read  and write data to file
import shelve

def save_to_long(url, id):
    s = shelve.open('long_to_id.db')
    try:
        s[url] = id
    finally:
        s.close()


def save_to_id(id, url):
    s = shelve.open('id_to_long.db')
    try:
        s[id] = url
        # print(s[id])
    finally:
        s.close()

def check_if_url_shortned(url):
    s = shelve.open('long_to_id.db')
    res = url in s
    s.close()

    return res

def check_if_id_present(id):
    s = shelve.open('id_to_long.db')
    res = id in s
    s.close()
    return res


def get_url(id):
    s = shelve.open('id_to_long.db')
    res = s[id]
    s.close()
    return res


def get_id(url):
    s = shelve.open('long_to_id.db')
    res = s[url]
    s.close()
    return res