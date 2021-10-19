# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.schema.email import Email
from plone.supermodel import model
from zope import schema

from zope.interface import implementer
from plone.autoform import directives
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.vocabularies.catalog import CatalogSource
from acentoweb.cnlse.vocabularies import LibrariesVocabulary

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.cnlse')


class ICNLSEResearcher(model.Schema):
    """ Marker interface for CNLSE Researcher
    """

    mail = Email(
        title=u'Mail',
        required=False,
        missing_value=u'',
    )
    
    relatedLibraries = RelationList(
        title=_(u'label_related_libraries', default=u'CNLSE Libraries'),
        default=[],
        value_type=RelationChoice(
            title=u'CNLSE Libraries',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )

    directives.widget(
        'relatedLibraries',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['cnlse_library', 'CNLSE Library']
            }
        )

@implementer(ICNLSEResearcher)
class CNLSEResearcher(Item):
    """
    """
