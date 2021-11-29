# -*- coding: utf-8 -*-
from acentoweb.cnlse.behaviors.collection_move import ICollectionMoveMarker
from acentoweb.cnlse.testing import ACENTOWEB_CNLSE_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class CollectionMoveIntegrationTest(unittest.TestCase):

    layer = ACENTOWEB_CNLSE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_collection_move(self):
        behavior = getUtility(IBehavior, 'acentoweb.cnlse.collection_move')
        self.assertEqual(
            behavior.marker,
            ICollectionMoveMarker,
        )
