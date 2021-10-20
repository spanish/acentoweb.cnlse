from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from plone import api

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.cnlse')

def format_title(folder):
    return "{}  ...   [ {} ]".format( folder.Title, folder.getURL())

def format_size(size):
    return size.encode('ascii', 'ignore')

def ResearchersVocabulary(context):

    cnlse_researchers = api.content.find(portal_type=['CNLSE Researcher', 'cnlse_researcher'], sort_on='sortable_title')

    if cnlse_researchers:
        terms = [ SimpleTerm(value=cnlse_researcher.UID, token=cnlse_researcher.UID, title=cnlse_researcher.Title) for cnlse_researcher in cnlse_researchers ]
    return SimpleVocabulary(terms)

directlyProvides(ResearchersVocabulary, IVocabularyFactory)

def PublishedResearchesVocabulary(context):

    cnlse_published_researches = api.content.find(portal_type=['CNLSE Library', 'cnlse_library'], sort_on='sortable_title')

    if cnlse_published_researches:
        terms = [ SimpleTerm(value=cnlse_library.UID, token=cnlse_library.UID, title=cnlse_library.Title) for cnlse_library in cnlse_published_researches ]
    return SimpleVocabulary(terms)

directlyProvides(PublishedResearchesVocabulary, IVocabularyFactory)

def UnpublishedResearchesVocabulary(context):

    cnlse_unpublished_researches = api.content.find(portal_type=['CNLSE Library', 'cnlse_library'], sort_on='sortable_title')

    if cnlse_unpublished_researches:
        terms = [ SimpleTerm(value=cnlse_library.UID, token=cnlse_library.UID, title=cnlse_library.Title) for cnlse_library in cnlse_unpublished_researches ]
    return SimpleVocabulary(terms)

directlyProvides(UnpublishedResearchesVocabulary, IVocabularyFactory)
