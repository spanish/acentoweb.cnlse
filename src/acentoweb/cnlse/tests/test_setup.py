# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from acentoweb.cnlse.testing import ACENTOWEB_CNLSE_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that acentoweb.cnlse is properly installed."""

    layer = ACENTOWEB_CNLSE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if acentoweb.cnlse is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'acentoweb.cnlse'))

    def test_browserlayer(self):
        """Test that IAcentowebCnlseLayer is registered."""
        from acentoweb.cnlse.interfaces import (
            IAcentowebCnlseLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IAcentowebCnlseLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ACENTOWEB_CNLSE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['acentoweb.cnlse'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if acentoweb.cnlse is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'acentoweb.cnlse'))

    def test_browserlayer_removed(self):
        """Test that IAcentowebCnlseLayer is removed."""
        from acentoweb.cnlse.interfaces import \
            IAcentowebCnlseLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IAcentowebCnlseLayer,
            utils.registered_layers())
