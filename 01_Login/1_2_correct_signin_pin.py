#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import os


import unittest

from com.dtmilano.android.viewclient import ViewClient, CulebraTestCase

TAG = 'CULEBRA'


class CulebraTests(CulebraTestCase):

    @classmethod
    def setUpClass(cls):
        cls.kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
        cls.kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': True}
        cls.options = {'start-activity': None, 'concertina': False, 'device-art': None, 'use-jar': False, 'multi-device': False, 'unit-test-class': True, 'save-screenshot': None, 'use-dictionary': False, 'glare': False, 'dictionary-keys-from': 'id', 'scale': 0.5, 'find-views-with-content-description': False, 'window': -1, 'orientation-locked': None, 'save-view-screenshots': None, 'find-views-by-id': True, 'log-actions': False, 'use-regexps': False, 'null-back-end': False, 'auto-regexps': None, 'do-not-verify-screen-dump': False, 'verbose-comments': False, 'gui': True, 'find-views-with-text': True, 'prepend-to-sys-path': False, 'drop-shadow': False, 'unit-test-method': None, 'interactive': False}
        cls.sleep = 0.3

    def setUp(self):
        super(CulebraTests, self).setUp()

    def tearDown(self):
        super(CulebraTests, self).tearDown()

    def preconditions(self):
        if not super(CulebraTests, self).preconditions():
            return False
        return True

    def testSomething(self):
        if not self.preconditions():
            self.fail('Preconditions failed')

        _s = CulebraTests.sleep
        _v = CulebraTests.verbose

        self.vc.dump(window=-1)

        print "Test Case: Login: Correct Credentials"

        # Enter Mobile Number
        self.vc.findViewById("com.sminq.businessbug:id/edit_text_mobile_number").setText('9393939393')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        # Login
        self.vc.findViewById("com.sminq.businessbug:id/button_login").touch()
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        # Verify PIN (Since PIN is set for Mobile number)
        self.vc.findViewByIdOrRaise("com.sminq.businessbug:id/edit_text_pin").setText('1111')
        self.vc.sleep(_s)
        self.vc.dump(window=-1)

        # Check for Correct Login
        if self.vc.findViewWithText(u'My Queues'):
            self.vc.sleep(_s)
            self.vc.dump(window=-1)
            self.vc.findViewWithContentDescription(u'''Open navigation drawer''').touch()
            self.vc.dump(window=-1)
            title = self.vc.findViewById("com.sminq.businessbug:id/text_view_title").getText()
            print "Passed! Logged in to '"+title+"' account"
            self.vc.findViewWithText(u'Home').touch()
            self.vc.dump(window=-1)
        else:
            print "Failed! Could not login."

if __name__ == '__main__':
    CulebraTests.main()
