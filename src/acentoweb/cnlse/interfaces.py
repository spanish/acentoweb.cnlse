# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
#from zope.interface import Interface
from z3c.form import interfaces
from zope import schema
from zope.interface import alsoProvides
from plone.supermodel import model
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('acentoweb.cnlse')



class IAcentowebCnlseLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""






class IAcentowebCnlseSettings(model.Schema):
    """Adds settings to medialog.controlpanel
    """

    model.fieldset(
        'voca',
        label=_(u'Vocabularies'),
        fields=[
             'territories',
             'classification'
             #other fields
        ],
     )




    territories = schema.List(
        title = _("label_territory", default=u"territory"),
        value_type=schema.TextLine()
    )

    classification = schema.List(
        title = _("label_classification", default=u"classification"),
        value_type=schema.TextLine()
    )



alsoProvides(IAcentowebCnlseSettings, IMedialogControlpanelSettingsProvider)
