# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
# pylint: disable=missing-docstring
# pylint: disable=too-many-public-methods

from __future__ import unicode_literals

from weechat_otr_test.weechat_otr_test_case import WeechatOtrTestCase

import weechat_otr

import sys

class IsAChannelTestCase(WeechatOtrTestCase):

    def test_hash(self):
        self.assertTrue(weechat_otr.is_a_channel('#channel', 'server'))

    def test_ampersand(self):
        self.add_channel_prefix('&')
        self.assertTrue(weechat_otr.is_a_channel('&channel', 'server'))

    def test_plus(self):
        self.add_channel_prefix('+')
        self.assertTrue(weechat_otr.is_a_channel('+channel', 'server'))

    def test_bang(self):
        self.add_channel_prefix('!')
        self.assertTrue(weechat_otr.is_a_channel('!channel', 'server'))

    def test_at(self):
        self.assertTrue(weechat_otr.is_a_channel('@#channel', 'server'))

    def test_not_a_channel(self):
        self.assertFalse(weechat_otr.is_a_channel('nick', 'server'))

    def test_hash_server_doesnt_isupport(self):
        self.server_no_chantypes()
        self.assertTrue(weechat_otr.is_a_channel('#channel', 'server'))

    def test_ampersand_server_doesnt_isupport(self):
        self.server_no_chantypes()
        self.assertTrue(weechat_otr.is_a_channel('&channel', 'server'))

    def test_plus_server_doesnt_isupport(self):
        self.server_no_chantypes()
        self.assertTrue(weechat_otr.is_a_channel('+channel', 'server'))

    def test_bang_server_doesnt_isupport(self):
        self.server_no_chantypes()
        self.assertTrue(weechat_otr.is_a_channel('!channel', 'server'))

    def test_at_server_doesnt_isupport(self):
        self.server_no_chantypes()
        self.assertTrue(weechat_otr.is_a_channel('@#channel', 'server'))

    def test_not_a_channel_server_doesnt_isupport(self):
        self.server_no_chantypes()
        self.assertFalse(weechat_otr.is_a_channel('nick', 'server'))

    def server_no_chantypes(self):
        sys.modules['weechat'].infos[
            ('server,CHANTYPES',)][
            'irc_server_isupport_value'] = ''
        sys.modules['weechat'].infos[
            ('server,STATUSMSG',)][
            'irc_server_isupport_value'] = ''

    def add_channel_prefix(self, prefix):
        sys.modules['weechat'].infos[
            ('server,CHANTYPES',)][
            'irc_server_isupport_value'] += prefix
