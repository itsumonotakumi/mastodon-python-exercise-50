import sys
from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id.txt'
token_file = 'access_token.txt'
username = 'itsumonotakumi@pawoo.net'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

# 対象アカウントのユーザーIDを取得する。
user_list = mastodon.account_search(username, limit=1)
user_id = user_list[0]['id']

# 対象アカウントの最新トゥート1件を取得する
user_toots = mastodon.account_statuses(user_id, limit=1)

# トゥートにお気に入り数によって処理を分岐する。
if user_toots[0]['favourited']:
    print(user_toots[0]['favourites_count'])
else:
    print('Not favourited')
