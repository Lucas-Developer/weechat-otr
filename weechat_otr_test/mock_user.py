# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

class MockUser(object):

    def __init__(self, nick):
        self.nick = nick

    def policy_config_option(self, _):
        # pylint: disable=no-self-use
        return ''
