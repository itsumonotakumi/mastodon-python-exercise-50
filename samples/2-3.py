from mastodon import Mastodon

url = sys.argv[1]
cid_file = 'client_id.txt'
token_file = 'access_token.txt'
img_filenames = ['img1.png', 'img2.png', 'img3.png', 'img4.png']

mastodon = Mastodon(
    client_id=cid_file,
    access_token=token_file,
    api_base_url=url
)

imgs = []
for img in img_filenames:
    imgs.append(mastodon.media_post(img))

mastodon.status_post(
    status='３回目のトゥート #Python練習',
    media_ids=imgs
    )
