import sys
from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id_pawoo.txt'
token_file = 'access_token_pawoo.txt'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

# 自分のアカウントのお気に入り数を数える
next_id = ''
fav_count = 0

# 自分のアカウントのお気に入り数を数える
while True:
    # ローカルタイムラインの取得
    fetched_favs = mastodon.favourites(limit=40, max_id=next_id)

    # 新しいトゥートが取得できなかったらループ終了
    if len(fetched_favs) > 0:
        fav_count += len(fetched_favs)
    else:
        break

    # 80件以上のページネーションするための値取得
    favs_last = fetched_favs[len(fetched_favs)-1]
    if '_pagination_next' in favs_last.keys() and 'max_id' in favs_last['_pagination_next'].keys():
        next_id = favs_last['_pagination_next']['max_id']
    else:
        break

# お気に入り数を表示
print(fav_count)
