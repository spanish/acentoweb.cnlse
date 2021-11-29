# -*- coding: utf-8 -*-
#Potential needed imports
from AccessControl import getSecurityManager
from Acquisition import aq_inner
from Acquisition import aq_parent
#from OFS.CopySupport import CopyError
#from Products.CMFCore.utils import getToolByName
#from Products.CMFPlone import PloneMessageFactory as _
#from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser import BrowserView
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
#from ZODB.POSException import ConflictError
#from z3c.form import button
#from z3c.form import field
#from z3c.form import form
#from z3c.form.widget import ComputedWidgetAttribute
from zExceptions import Unauthorized
#from zope import schema
#from zope.component import getMultiAdapter
#from zope.component import queryMultiAdapter
#from zope.container.interfaces import INameChooser
from zope.event import notify
from zope.interface import Interface
#from zope.lifecycleevent import ObjectModifiedEvent

#import six
import transaction


from plone import api



class CollectionMove(BrowserView):

    def __call__(self):
        messages = IStatusMessage(self.request)
        context = self.context

        #Get folder we move the images to
        to_folder = context.linked_folder.to_object

        ## TO DO: Check if any item is locked ??
        #plone.api.content.move(source=None, target=None, id=None, safe_id=False)[source]¶
        #Move the object to the target container.

        #Parameters
        #source (Content object) – [required] Object that we want to move.
        #target (Folderish content object) – Target container to which the source object will be moved. If no target is specified, the source object’s container will be used as a target, effectively making this operation a rename (Rename content).
        #id (string) – Pass this parameter if you want to change the id of the moved object on the target location. If the new id conflicts with another object in the target container, a suffix will be added to the moved object’s id.
        #safe_id (boolean) – When False, the given id will be enforced. If the id is conflicting with another object in the target container, raise a InvalidParameterError. When True, choose a new, non-conflicting id.

        #Returns
        #Content object that was moved to the target location

        #Raises
        #KeyError ValueError

        #portal = api.portal.get()

        #except KeyError:
        #    messages.add(u"Folder does not exist", type="warning")

        if to_folder:

            for item in  context.restrictedTraverse('@@contentlisting')():
                try:
                    api.content.move(source=item.getObject(), target=to_folder)
                    messages.add('Moved item: ' + item.id, type="info")
                except KeyError:
                    messages.add(u"Folder does not exist", type="warning")

        else:
            messages.add(u'Nothing to move', type="info")

        self.request.response.redirect(context.absolute_url())
