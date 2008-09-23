"""
A module containing the Tiddler class and related functions.
"""

from datetime import datetime


def current_timestring():
    """
    Translate (now) into a TiddlyWiki conformat timestring.
    """
    time_object = datetime.utcnow()
    return unicode(time_object.strftime('%Y%m%d%H%M'))


class Tiddler(object):
    """
    The universal content object in the TiddlyWiki
    universe, corresponding to a Page in other wiki
    systems. A Tiddler has text and some associated
    metadata. The text can be anything, but is usually
    wikitext in some form, or Javascript code to be
    used as a plugin.

    Tiddler is intentional just a container of data.
    That is, it has no methods which change the state
    of attributes in the Tiddler or manipulate the tiddler.
    Changing the attributes is done by directly changing
    the attributes. This is done to make the Tiddler
    easier to store and serialize in a diversity of ways.

    A Tiddler has several attributes:

    title: The name of the tiddler. Required.
    created: A string representing when this tiddler was
            created.
    modified: A string representing when this tiddler was
             last changed. Defaults to now.
    modifier: A string representing a personage that changed
              this tiddler in some way. This doesn't necessarily
              have any assocation with the tiddlyweb.usersign,
              though it may.
    tags: A list of strings that describe the tiddler.
    fields: An arbitrary dictionary of extended fields on the tiddler.
    text: The contents of the tiddler. A string.
    revision: The revision of this tiddler. An int.
    bag: The name of the bag in which this tiddler exists,
         if any. Usually set by internal code.
    recipe: The name of the recipe in which this tiddler exists,
            if any. Usually set by internal code.
    store: A reference to the Store object which retrieved
           this tiddler from persistent storage.
    """

    __slots__ = ['title',
            'created',
            'modified',
            'modifier',
            'tags',
            'fields',
            'text',
            'revision',
            'bag',
            'recipe',
            'store']

    def __init__(self,
            title=None,
            bag=None):
        """
        Create a new Tiddler object.

        A title is required to ceate a tiddler.
        """
        self.title = title
        self.bag = bag

        self.created = ''
        self.modified = current_timestring()
        self.modifier = None
        self.tags = []
        self.fields = {}
        self.text = None
        self.revision = None
        self.recipe = None
        # reference to the store which 'got' us
        # this is can be used in serialization
        self.store = None

    def __repr__(self):
        """
        Make the printed tiddler include the title so we
        can distinguish between them while debugging.
        """
        return self.title + object.__repr__(self)
