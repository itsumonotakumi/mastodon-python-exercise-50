from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id.txt'
token_file = 'access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

# 最新トゥートのお気に入りを解除する
user_dict = mastodon.account_verify_credentials()
user_toots_dict = mastodon.account_statuses(user_dict['id'], limit=1)
mastodon.status_unfavourite(user_toots_dict[0]['id'])
