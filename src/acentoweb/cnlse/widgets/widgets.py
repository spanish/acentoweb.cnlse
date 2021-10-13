from plone.app.z3cform.widget import RelatedItemsWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.widget import FieldWidget
from zope.interface import implementer

@implementer(IFieldWidget)
def RelatedItemsFieldWidget(field, request, extra=None):
    if extra is not None:
        request = extra
    field.vocabularyName = 'plone.app.vocabularies.Catalog'
    return FieldWidget(field, RelatedItemsWidget(request))
