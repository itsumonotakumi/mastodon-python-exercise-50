import sys
import re
from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id.txt'
token_file = 'access_token.txt'
conv = re.compile(r"<[^>]*?>")
toot_num = 10  # 取得するトゥートの件数
hashtag = 'こんなマストドンは嫌だ'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

# インスタンスのローカルタイムラインのトゥートを10件表示する
toots = mastodon.timeline_hashtag(hashtag)
for i in range(0, toot_num):
    toot_text = conv.sub("", toots[i]['content'])
    print("{:%Y-%m-%d %H:%M:%S}, {}".format(toots[i]['created_at'], toot_text))
