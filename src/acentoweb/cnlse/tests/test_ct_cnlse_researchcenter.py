# -*- coding: utf-8 -*-
from acentoweb.cnlse.testing import ACENTOWEB_CNLSE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class CNLSEResearchcenterIntegrationTest(unittest.TestCase):

    layer = ACENTOWEB_CNLSE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_cnlse_researchcenter_schema(self):
        fti = queryUtility(IDexterityFTI, name='CNLSE Researchcenter')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('CNLSE Researchcenter')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_cnlse_researchcenter_fti(self):
        fti = queryUtility(IDexterityFTI, name='CNLSE Researchcenter')
        self.assertTrue(fti)

    def test_ct_cnlse_researchcenter_factory(self):
        fti = queryUtility(IDexterityFTI, name='CNLSE Researchcenter')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_cnlse_researchcenter_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='CNLSE Researchcenter',
            id='cnlse_researchcenter',
        )


        parent = obj.__parent__
        self.assertIn('cnlse_researchcenter', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('cnlse_researchcenter', parent.objectIds())

    def test_ct_cnlse_researchcenter_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='CNLSE Researchcenter')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
