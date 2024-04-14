from collections.abc import MutableMapping

class MapBase(MutableMapping):

    '''' An abstract base class that includes a nonpublic _Item class'''

    class _Item:
        ''' A lightweight composite to store ke-value pairs as map
        items'''

        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._v = v
        
        def __eq__(self, other):
            return self._key == other._key
        
        def __ne__(self, other):
            return not(self == other)
        
        def __lt__(self, other):
            return self._key < other._key
        

    