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
from acentoweb.cnlse.vocabulary import LibrariesVocabulary

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.cnlse')


class ICNLSEResearchcenter(model.Schema):
    """ Marker interface for CNLSE Researchcenter
    """

    mail = Email(
        title=u'Mail',
        required=False,
        missing_value=u'',
    )

    web = schema.URI(
        title=u'Web',
        required=False,
        missing_value=u'',
    )

    territories = schema.List (
        title = _("Territories", default=u"Territories"),
        value_type=schema.Choice(
            title = _("Territory", default=u"Territory"),
            required = False,
            vocabulary = 'acentoweb.cnlse.TerritoryVocabulary'
        )
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

    relatedResearchers = RelationList(
        title=_(u'label_related_researchers', default=u'CNLSE Researchers'),
        default=[],
        value_type=RelationChoice(
            title=u'CNLSE Researchers',
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

    directives.widget(
        'relatedResearchers',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['cnlse_researcher', 'CNLSE Researcher']
            }
        )

@implementer(ICNLSEResearchcenter)
class CNLSEResearchcenter(Item):
    """
    """
