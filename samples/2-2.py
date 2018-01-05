from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id.txt'
token_file = 'access_token.txt'
imgfile1 = 'img1.png'

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

img1 = mastodon.media_post(imgfile1)

img_files = [img1]
mastodon.status_post(
    status='はじめてのトゥート2 #Python練習',
    media_ids=img_files
    )
