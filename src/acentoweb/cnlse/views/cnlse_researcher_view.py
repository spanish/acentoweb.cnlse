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


class CNLSEResearcherView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('cnlse_researcher_view.pt')

    def __call__(self):
        # Implement your own actions:
        #self.msg = _(u'A small message')
        return self.index()

    def get_relatedresearchers(self, context = None):

        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items

    #Both relations'ways' are kept, in case you want to refer 'the other way around later'
    #see cnlse_library_view.py
    #Note, if you only want back references of a certain content type: please look at code in cnlse_library.py

    def get_relatedlibraries(self):
        """Returns libraries"""
        refs = (self.context.relatedLibraries)
        to_objects = [ref.to_object for ref in refs if not ref.isBroken()]
        refers = self.get_referers(self.context)
        from_objects = [ref.from_object for ref in refers if not ref.isBroken()]
        ref_list = to_objects + from_objects
        return OrderedDict( (x,1) for x in ref_list ).keys()

    def get_referers(self, context = None):
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
