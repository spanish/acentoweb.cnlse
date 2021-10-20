# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.schema.email import Email
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from zope import schema

from zope.interface import implementer
from plone.autoform import directives
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.app.vocabularies.catalog import CatalogSource
from acentoweb.cnlse.vocabularies import ResearchersVocabulary
from acentoweb.cnlse.vocabularies import PublishedResearchesVocabulary
from acentoweb.cnlse.vocabularies import UnpublishedResearchesVocabulary

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.cnlse')


class ICNLSEResearchcenter(model.Schema):
    """ Marker interface for CNLSE Researchcenter
    """

    fieldset(
        'drupal',
        label=u'Drupal fields',
        fields=('drupal_image', 'drupal_video'),
    )

    drupal_image = schema.TextLine(
        title=_(u'label_drupal_image', default=u'Drupal image'),
        required=False,
    )

    drupal_video = schema.TextLine(
        title=_(u'label_drupal_video', default=u'Drupal video'),
        required=False,
    )

    image = NamedBlobImage(
        title=_(u'label_image', default=u'Image'),
        description=_(u'label_image_description', default=u'Main image'),
        required=False,
        )

    video = NamedBlobFile(
        title=_(u'label_video', default=u'Video'),
        description=_(u'label_video_description', default=u'Main video'),
        required=False,
        )

    territory = schema.Choice(
        title = _("label_territory", default=u"Territory"),
        description=_(u'label_territory_description', default=u'Territorial scope'),
        vocabulary = 'collective.taxonomy.cnlse_resource_territory'
    )

    address = schema.TextLine(
        title=_(u'label_address', default=u'Address'),
        required=True,
    )

    phone = schema.TextLine(
        title=_(u'label_phone', default=u'Phone'),
        required=False,
    )

    fax = schema.TextLine(
        title=_(u'label_fax', default=u'Fax'),
        required=False,
    )

    email = Email(
        title=_(u'label_email', default=u'Email'),
        required=False,
        missing_value=u'',
    )

    web = schema.URI(
        title=_(u'label_web', default=u'Web'),
        required=False,
        missing_value=u'',
    )

    others = RichText(
        title=_(u'label_others', default=u'Others'),
        required=False,
        )

    research_lines_classification = schema.List (
        title = _("label_research_lines_classification", default=u"Research lines: Classification"),
        value_type=schema.Choice(
            title = _("label_research_lines_classification", default=u"Research lines: Classification"),
            vocabulary = 'collective.taxonomy.cnlse_research_lines',
            required = False
        )
    )

    research_lines_names = RichText(
        title=_(u'label_research_lines_names', default=u'Research lines: Names'),
        required=False,
        )

    projects = RichText(
        title=_(u'label_projects', default=u'Projects'),
        required=False,
        )

    more_information = RichText(
        title=_(u'label_more_information', default=u'More information'),
        required=False,
        )

    relatedResearchers = RelationList(
        title=_(u'label_related_researchers', default=u'Researchers'),
        default=[],
        value_type=RelationChoice(
            title=u'Researchers',
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )

    relatedPublishedResearches = RelationList(
        title=_(u'label_related_published_researches', default=u'Published researches'),
        default=[],
        value_type=RelationChoice(
            title=_(u'label_related_published_researches', default=u'Published researches'),
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )

    relatedUnpublishedResearches = RelationList(
        title=_(u'label_related_unpublished_researches', default=u'Unpublished researches'),
        default=[],
        value_type=RelationChoice(
            title=_(u'label_related_unpublished_researches', default=u'Unpublished researches'),
            vocabulary='plone.app.vocabularies.Catalog',
        ),
        required=False,
    )

    directives.widget(
        'relatedResearchers',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['cnlse_researcher', 'CNLSE Researcher']
            }
        )

    directives.widget(
        'relatedPublishedResearches',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['cnlse_library', 'CNLSE Library']
            }
        )

    directives.widget(
        'relatedUnpublishedResearches',
        RelatedItemsFieldWidget,
        pattern_options={
            'selectableTypes': ['cnlse_library', 'CNLSE Library']
            }
        )

@implementer(ICNLSEResearchcenter)
class CNLSEResearchcenter(Item):
    """
    """
