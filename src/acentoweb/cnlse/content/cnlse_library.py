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

class ICNLSELibrary(model.Schema):
    """ Marker interface and Dexterity Python Schema for CNLSE Library
    """

    fieldset(
        'drupal',
        label=u'Drupal fields',
        fields=('drupal_image', 'drupal_video', 'drupal_attachment'),
    )

    drupal_image = schema.TextLine(
        title=_(u'label_drupal_image', default=u'Drupal image'),
        required=False,
    )

    drupal_video = schema.TextLine(
        title=_(u'label_drupal_video', default=u'Drupal video'),
        required=False,
    )

    drupal_attachment = schema.TextLine(
        title=_(u'label_drupal_attachment', default=u'Drupal attachment'),
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

    attachment = NamedBlobFile(
        title=_(u'label_attachment', default=u'Attachment'),
        description=_(u'label_attachment_description', default=u'Main attachment'),
        required=False,
        )

    details = RichText(
        title=_(u'label_details', default=u'Details'),
        required=True,
        )

    author = schema.TextLine(
        title=_(u'label_author', default=u'Author'),
        required=True,
    )

    year = schema.TextLine(
        title=_(u'label_year', default=u'Year'),
        required=True,
    )

    publisher = schema.TextLine(
        title=_(u'label_publisher', default=u'Publisher'),
        required=True,
    )

    collection = schema.TextLine(
        title=_(u'label_collection', default=u'Collection'),
        required=False,
    )

    code_type = schema.Choice(
        title=_(u'label_code_type', default=u'Code type'),
        vocabulary = 'collective.taxonomy.cnlse_library_code_type'
    )

    code = schema.TextLine(
        title=_(u'label_code', default=u'Code'),
        required=False,
    )

    topics = schema.List(
        title = _("label_library_topics", default=u"Topics"),
        value_type=schema.Choice(
            title = _("label_library_topics", default=u"Topics"),
            vocabulary = 'collective.taxonomy.cnlse_library_topics',
            required = False
        )
    )

    support = schema.Choice(
        title=_(u'label_support', default=u'Support'),
        vocabulary = 'collective.taxonomy.cnlse_support',
        required=True
    )

    ubication = RichText(
        title=_(u'label_ubication', default=u'Ubication'),
        required=False,
        )

@implementer(ICNLSELibrary)
class CNLSELibrary(Item):
    """
    """
