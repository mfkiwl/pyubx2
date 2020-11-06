'''
Created on 3 Oct 2020

Parse method tests for pyubx2.UBXMessage

@author: semuadmin
'''
# pylint: disable=line-too-long, no-member

import unittest

from pyubx2 import UBXMessage, SET, POLL, GET


class ParseTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.ack_ack = b'\xb5b\x05\x01\x02\x00\x06\x01\x0f\x38'
        self.ack_ack_badck = b'\xb5b\x05\x01\x02\x00\x06\x01\x0f\x37'
        self.cfg_msg = b'\xb5b\x06\x01\x08\x00\xf0\x01\x00\x01\x01\x01\x00\x00\x036'
        self.cfg_prt = b'\xb5b\x06\x00\x00\x00\x06\x18'
        self.nav_velned = b'\xb5b\x01\x12$\x000D\n\x18\xfd\xff\xff\xff\xf1\xff\xff\xff\xfc\xff\xff\xff\x10\x00\x00\x00\x0f\x00\x00\x00\x83\xf5\x01\x00A\x00\x00\x00\xf0\xdfz\x00\xd0\xa6'
        self.nav_svinfo = b''

    def tearDown(self):
        pass

    def testAck(self):
        res = UBXMessage.parse(self.ack_ack, True)
        self.assertIsInstance(res, UBXMessage)

    def testAckID(self):
        res = UBXMessage.parse(self.ack_ack, True)
        self.assertEqual(res.identity, 'ACK-ACK')

    def testAckStr(self):
        res = UBXMessage.parse(self.ack_ack, True)
        self.assertEqual(str(res), '<UBX(ACK-ACK, clsID=CFG, msgID=CFG-MSG)>')

    def testAckRepr(self):
        res = UBXMessage.parse(self.ack_ack, True)
        self.assertEqual(repr(res), "'UBXMessage(b'\\x05', b'\\x01', 0, payload=b'\\x06\\x01')'")

    def testAckCkF(self):
        UBXMessage.parse(self.ack_ack_badck, False)

    def testCfg(self):
        res = UBXMessage.parse(self.ack_ack, True)
        self.assertIsInstance(res, UBXMessage)

    def testCfgID(self):
        res = UBXMessage.parse(self.cfg_msg, True)
        self.assertEqual(res.identity, 'CFG-MSG')

    def testCfgStr(self):
        res = UBXMessage.parse(self.cfg_msg, True)
        self.assertEqual(str(res), '<UBX(CFG-MSG, msgClass=NMEA-Standard, msgID=GLL, rateDDC=0, rateUART1=1, rateUART2=1, rateUSB=1, rateSPI=0, reserved=0)>')

    def testCfgRepr(self):
        res = UBXMessage.parse(self.cfg_msg, True)
        self.assertEqual(repr(res), "'UBXMessage(b'\\x06', b'\\x01', 0, payload=b'\\xf0\\x01\\x00\\x01\\x01\\x01\\x00\\x00')'")

    def testCfgProp1(self):
        res = UBXMessage.parse(self.cfg_msg, True)
        self.assertEqual(res.rateUART1, 1)

    def testCfgProp2(self):
        res = UBXMessage.parse(self.cfg_msg, True)
        self.assertEqual(res.rateSPI, 0)

    def testNavVelNed(self):
        res = UBXMessage.parse(self.nav_velned, True)
        self.assertIsInstance(res, UBXMessage)

    def testNavVelNedID(self):
        res = UBXMessage.parse(self.nav_velned, True)
        self.assertEqual(res.identity, 'NAV-VELNED')

    def testNavVelNedStr(self):
        res = UBXMessage.parse(self.nav_velned, True)
        self.assertEqual(str(res), '<UBX(NAV-VELNED, iTOW=16:01:50, velN=-3, velE=-15, velD=-4, speed=16, gSpeed=15, heading=128387, sAcc=65, cAcc=8052720)>')

    def testNavVelNedRepr(self):
        res = UBXMessage.parse(self.nav_velned, True)
        self.assertEqual(repr(res), "'UBXMessage(b'\\x01', b'\\x12', 0, payload=b'0D\\n\\x18\\xfd\\xff\\xff\\xff\\xf1\\xff\\xff\\xff\\xfc\\xff\\xff\\xff\\x10\\x00\\x00\\x00\\x0f\\x00\\x00\\x00\\x83\\xf5\\x01\\x00A\\x00\\x00\\x00\\xf0\\xdfz\\x00')'")

    def testNavVelNedProp1(self):
        res = UBXMessage.parse(self.nav_velned, True)
        self.assertEqual(res.iTOW, 403326000)

    def testNavVelNedProp2(self):
        res = UBXMessage.parse(self.nav_velned, True)
        self.assertEqual(res.cAcc, 8052720)

    def testCfgPrt(self):  # POLL example with null payload
        res = UBXMessage.parse(self.cfg_prt, True)
        self.assertIsInstance(res, UBXMessage)

    def testCfgPrtID(self):
        res = UBXMessage.parse(self.cfg_prt, True)
        self.assertEqual(res.identity, 'CFG-PRT')

    def testCfgPrtStr(self):
        res = UBXMessage.parse(self.cfg_prt, True)
        self.assertEqual(str(res), '<UBX(CFG-PRT)>')

    def testCfgPrtRepr(self):
        res = UBXMessage.parse(self.cfg_prt, True)
        self.assertEqual(repr(res), "'UBXMessage(b'\\x06', b'\\x00', 0)'")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
