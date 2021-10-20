# -*- coding: utf-8 -*-

from acentoweb.cnlse import _

# from Products.Five.browser import BrowserView
# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

#We use DefaultView instead of BrowserView so we can use the taxonomy widgets directly
# https://community.plone.org/t/can-i-render-ollective-taxonomy-field-directly-in-template-pt-tal/14403/2
from plone.dexterity.browser.view import DefaultView

from zc.relation.interfaces import ICatalog
from collections import OrderedDict
from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission

class CNLSEResearchcenterView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('cnlse_researchcenter_view.pt')

    #def __call__(self):
    #    # Implement your own actions:
    #    #self.msg = _(u'A small message')
    #    return self.index()

    #Both relations'ways' are kept, in case you want to refer 'the other way around later'
    #see cnlse_library_view.py
    #Note, if you only want back references of a certain content type: please look at code in cnlse_library.py

    def get_relatedresearchers(self):
        """Returns researchers"""
        refs = self.context.relatedResearchers
        to_objects = [ref.to_object for ref in refs if not ref.isBroken()]
        refers = self.get_referers(self.context)
        from_objects = [ref.from_object for ref in refers if not ref.isBroken()]
        ref_list = to_objects + from_objects
        return OrderedDict( (x,1) for x in ref_list ).keys()

    def get_relatedpublishedresearches(self):
        """Returns published researches"""
        refs = (self.context.relatedPublishedResearches)
        to_objects = [ref.to_object for ref in refs if not ref.isBroken()]
        refers = self.get_referers(self.context)
        from_objects = [ref.from_object for ref in refers if not ref.isBroken()]
        ref_list = to_objects + from_objects
        return OrderedDict( (x,1) for x in ref_list ).keys()

    def get_relatedunpublishedresearches(self):
        """Returns unpublished researches"""
        refs = (self.context.relatedUnpublishedResearches)
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
