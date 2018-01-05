from mastodon import Mastodon

url = 'https://HOSTNAME/'
appname = 'Python_Exercise'
cid_file = 'client_id.txt'

Mastodon.create_app(
    appname,
    api_base_url= rl,
    to_file=cid_file
)
