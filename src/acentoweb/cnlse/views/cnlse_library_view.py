# -*- coding: utf-8 -*-

from acentoweb.cnlse import _
from Products.Five.browser import BrowserView
from zc.relation.interfaces import ICatalog
from collections import OrderedDict

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class CNLSELibraryView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('cnlse_library_view.pt')

    def __call__(self):
        return self.index()

    def get_relatedlibraries(self, context = None):

        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items

    def back_researchcenters(self, context = None ):
        """
        Return referenced researchcenters
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        result= []
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        for rel in list(catalog.findRelations(rel_query)):
            obj = intids.queryObject(rel.from_id)
            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'CNLSE Researchcenter' :
                    result.append(obj)
        return result

    def back_researchers(self, context = None ):
        """
        Return referenced researchers
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        result= []
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        for rel in list(catalog.findRelations(rel_query)):
            obj = intids.queryObject(rel.from_id)
            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'CNLSE Researcher' :
                    result.append(obj)
        return result
