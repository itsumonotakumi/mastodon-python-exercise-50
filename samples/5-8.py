import sys
from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id.txt'
token_file = 'access_token.txt'
username = 'itsumonotakumi@pawoo.net'

mastodon = Mastodon(
    client_idcid_file,
    access_tokentoken_file,
    api_base_urlurl
)

# 対象アカウントのユーザーIDを取得する。
user_list = mastodon.account_search(username, limit=1)
user_id = user_list[0]['id']

# 対象アカウントの最新トゥート10件を取得する
user_toots = mastodon.account_statuses(user_id, limit=1)

# トゥートの時間と内容を表示する
print(user_toots[0]['created_at'], user_toots[0]['content'])
