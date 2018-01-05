from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id.txt'
token_file = 'access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

# 自分の最新トゥート10件を表示する
user_dict = mastodon.account_verify_credentials()
user_toots = mastodon.account_statuses(user_dict['id'], limit=10)
print(user_toots)
