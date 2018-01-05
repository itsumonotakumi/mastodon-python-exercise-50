from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id.txt'
token_file = 'access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

# 自分の最新トゥート1件を取得する
user_dict = mastodon.account_verify_credentials()
user_toots = mastodon.account_statuses(user_dict['id'], limit=1)

# トゥートの時間と内容を表示する
print(user_toots[0]['created_at'], user_toots[0]['content'])
