
from typing import Any
from template import MapBase

class UnsortedTableMap(MapBase):

    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __len__(self) -> int:
        """Return number of items in the map."""
        return len(self._table)
    
    def __iter(self):
        """Genrate iteration of the map's keys."""
        for item in self.table:
            return item._key

    def __getitem__(self, k):
        """Return value for key: k and raise a key error if not found"""

        for item in self._table:
            if k == item._key:
                return item._value
            raise KeyError('Key Error: ' + repr(k))
        

    def __setitem__(self, key: Any, value: Any) -> None:
        """Set the value for a key in the inner table. If the key does not exist 
        intantiate an item and add append it to the table."""
        for item in self._table:
            if key == item._key:
                item._value = value
                return
        
        self._table.append(self._Item(key, value))
        return
    

    def __delitem__(self, key: Any) -> None:
        """iterate over the table looking for the key provided. 
        If the key is found pop it from the table. Otherwise raise KeyErrror"""
        for j in range(len(self._table)):
            if key == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError("Key Error: %r" % key)
    

