import json
import urllib.request


def pages(limit=10, page=1):
    cur = page
    while True:
        url = 'https://danbooru.donmai.us/posts.json?limit={}&page={}'.format(limit, cur)
        res = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
        for post in res:
            yield post
        cur += 1

p = pages(limit=100)
while True:
    post = next(p)
    if 'file_url' in post.keys():
        if post['rating'] == 'e':
            loc = 'Download\\{}.jpg'.format(post['id'])
            print('downloading {} in {}...'.format(post['id'], loc))
            urllib.request.urlretrieve('https://danbooru.donmai.us{}'.format(post['file_url']), loc)
