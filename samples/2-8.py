from mastodon import Mastodon

url = 'HOSTNAME'
cid_file = 'client_id.txt'
token_file = 'access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

mastodon.status_post(
    '@test@itumonotakumi.m.to はじめてのダイレクトトゥート #Python練習',
    visibility='direct'
    )
