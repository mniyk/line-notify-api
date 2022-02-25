"""LINE Notifyを操作するためのモジュール
"""
import requests


class LineNotify():
    def __init__(self, access_token: str) -> None:
        """初期化

        Args:
            access_token (str): Web APIのアクセストークン

        Examples:
            >>> api = LineNotify(
                    access_token=config.get('LINE_NOTIFY', 'ACCESS_TOKEN'))
        """
        self.url = 'https://notify-api.line.me/api/notify'
        self.access_token = access_token

    def send_message(self, message: str):
        """メッセージの送信

        Args:
            message (str): メッセージ

        Examples:
            >>> api.send_message('Test Line Notify')
        """
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {'message': f'\n{message}'}

        response = requests.post(self.url, headers=headers, data=data)

        return response
