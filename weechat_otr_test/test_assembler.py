from __future__ import unicode_literals

from weechat_otr_test.weechat_otr_test_case import WeechatOtrTestCase

import weechat_otr

class AssemblerTestCase(WeechatOtrTestCase):

    def afterSetUp(self):
        self.assembler = weechat_otr.Assembler()

    def test_is_query_start(self):
        self.assembler.add('?OTRv2? encryption?')

        self.assertTrue(self.assembler.is_query())

    def test_is_query_middle(self):
        self.assembler.add('ATT: ?OTRv2?someone requested encryption!')

        self.assertTrue(self.assembler.is_query())

    def test_is_query_end(self):
        self.assembler.add('encryption? ?OTRv2?')

        self.assertTrue(self.assembler.is_query())
