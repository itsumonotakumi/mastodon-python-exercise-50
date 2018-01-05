import sys
from mastodon import Mastodon

URL = sys.argv[1]
CID_FILE = 'client_id.txt'
TOKEN_FILE = 'access_token.txt'
USERNAME = 'itsumonotakumi@pawoo.net'


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

    # 対象アカウントのユーザーIDを取得する。
    user_list = mastodon.account_search(USERNAME, limit=1)
    user_id = user_list[0]['id']

    # 対象アカウントの最新トゥート10件を取得する
    user_toots = mastodon.account_statuses(user_id, limit=1)
        
    # トゥートのアプリ名があれば表示する
    if user_toots[0]['reblog'] is None:
        print(check_appname(user_toots[0]))            # 通常のトゥートの場合
    else:
        print(check_appname(user_toots[0]['reblog']))  # ブーストされたトゥートの場合

if __name__ == '__main__':
    main()
