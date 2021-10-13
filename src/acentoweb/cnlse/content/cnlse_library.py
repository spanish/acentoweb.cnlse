# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

# from acentoweb.cnlse import _

class ICNLSELibrary(model.Schema):
    """ Marker interface and Dexterity Python Schema for CNLSE Library
    """

@implementer(ICNLSELibrary)
class CNLSELibrary(Item):
    """
    """
