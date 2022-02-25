"""line_notify.pyのunittest
"""
import configparser
import logging
import unittest

from line_notify import LineNotify


logging.basicConfig(
    level=logging.INFO,
    format='\t'.join([
        '%(asctime)s',
        '%(levelname)s',
        '%(filename)s',
        '%(funcName)s',
        '%(processName)s',
        '%(process)d',
        '%(threadName)s',
        '%(thread)d',
        '%(message)s']))
logger = logging.Logger(__name__)


class TestLineNotify(unittest.TestCase):
    def setUp(self) -> None:
        config = configparser.ConfigParser()
        config.read('settings.ini')

        self.api = LineNotify(
            access_token=config.get('LINE_NOTIFY', 'ACCESS_TOKEN'))

    def test_send_message(self) -> None:
        response = self.api.send_message("Test Line Notify")

        print(response)
