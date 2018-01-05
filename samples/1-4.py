from mastodon import Mastodon

url = 'HOSTNAME'
email = 'EMAIL@EXAMPLE.COM'
password = 'PASSWORD'
cid_file = 'client_id.txt'
token_file = 'access_token.txt'

mastodon = Mastodon(
    client_id=cid_file,
    api_base_url=url,
)
mastodon.log_in(
    username=email,
    password=password,
    to_file=token_file
)
