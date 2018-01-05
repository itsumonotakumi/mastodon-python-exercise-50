import sys
import re
from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client.txt'
token_file = 'access_token.txt'
conv = re.compile(r"<[^>]*?>")
toot_num = 100  # 取得するトゥートの件数
hashtag = 'こんなマストドンは嫌だ'  # ハッシュタグの指定

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

# 指定したハッシュタグのついたトゥートを100件表示する
next_id = ''
toots = []''

while (len(toots) < toot_num):
    # ハッシュタグのついたトゥートの取得
    fetched_toots = mastodon.timeline_hashtag(
        hashtag=hashtag,
        local=False,
        limit=80,
        max_id=next_id
    )
    
    # 新しいトゥートが取得できなかったらループ終了
    if len(fetched_toots) > 0:
        toots += fetched_toots
    else:
        break

    # 80件以上のページネーションするための値取得
    toots_last = len(toots)-1
    if toots[toots_last]['_pagination_next']['max_id'] is not None:
        next_id = toots[toots_last]['_pagination_next']['max_id']
    else:
        break

# 表示するトゥート数の上限を指定
max_len = toot_num if toot_num < len(toots) else len(toots)

# トゥートを整形して表示する
for i in range(0, max_len):
    toot_text = conv.sub("", toots[i]['content'])
    print("{}, {:%Y-%m-%d %H:%M:%S}, {}".format(
        i+1,
        toots[i]['created_at'],
        toot_text
        )
    )
