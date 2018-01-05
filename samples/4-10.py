import sys
from mastodon import Mastodon

URL = sys.argv[1]
CID_FILE = 'client_id.txt'
TOKEN_FILE = 'access_token.txt'


def check_appname(toot):
    ''' アプリケーション名をチェックするルーチン '''
    if toot['application'] and toot['application']['name']:
        return(toot['application']['name'])
    elif toot['application'] and not toot['application']['name']:
        return('Web')
    else:
        return('Unknown')
        

def main():
    ''' メインルーチン '''
    # Mastodon初期化
    mastodon = Mastodon(
        client_id=CID_FILE,
        access_token=TOKEN_FILE,
        api_base_url=URL
    )
    
    # 自分の最新トゥート1件を取得する
    user_dict = mastodon.account_verify_credentials()
    user_toots = mastodon.account_statuses(user_dict['id'], limit=1)
    
    # トゥートのアプリ名があれば表示する
    if user_toots[0]['reblog'] is None:
        print(check_appname(user_toots[0]))            # 通常のトゥートの場合
    else:
        print(check_appname(user_toots[0]['reblog']))  # ブーストされたトゥートの場合
 

if __name__ == '__main__':
    main()
