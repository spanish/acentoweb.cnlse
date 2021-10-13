# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import acentoweb.cnlse


class AcentowebCnlseLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=acentoweb.cnlse)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'acentoweb.cnlse:default')


ACENTOWEB_CNLSE_FIXTURE = AcentowebCnlseLayer()


ACENTOWEB_CNLSE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ACENTOWEB_CNLSE_FIXTURE,),
    name='AcentowebCnlseLayer:IntegrationTesting',
)


ACENTOWEB_CNLSE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ACENTOWEB_CNLSE_FIXTURE,),
    name='AcentowebCnlseLayer:FunctionalTesting',
)


ACENTOWEB_CNLSE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ACENTOWEB_CNLSE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='AcentowebCnlseLayer:AcceptanceTesting',
)
