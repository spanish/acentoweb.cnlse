# -*- coding: utf-8 -*-
from acentoweb.cnlse.content.cnlse_library import ICNLSELibrary  # NOQA E501
from acentoweb.cnlse.testing import ACENTOWEB_CNLSE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class CNLSELibraryIntegrationTest(unittest.TestCase):

    layer = ACENTOWEB_CNLSE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_cnlse_library_schema(self):
        fti = queryUtility(IDexterityFTI, name='CNLSE Library')
        schema = fti.lookupSchema()
        self.assertEqual(ICNLSELibrary, schema)

    def test_ct_cnlse_library_fti(self):
        fti = queryUtility(IDexterityFTI, name='CNLSE Library')
        self.assertTrue(fti)

    def test_ct_cnlse_library_factory(self):
        fti = queryUtility(IDexterityFTI, name='CNLSE Library')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICNLSELibrary.providedBy(obj),
            u'ICNLSELibrary not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_cnlse_library_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='CNLSE Library',
            id='cnlse_library',
        )

        self.assertTrue(
            ICNLSELibrary.providedBy(obj),
            u'ICNLSELibrary not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('cnlse_library', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('cnlse_library', parent.objectIds())

    def test_ct_cnlse_library_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='CNLSE Library')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
