from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id.txt'
token_file = 'access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

mastodon.toot('はじめてのトゥート #Python練習')
