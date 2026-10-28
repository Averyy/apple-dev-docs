# iteratorSize

**Framework**: Kernel  
**Kind**: instm

Returns the size in bytes of a subclass's iteration context.

## Declaration

```cpp
virtual unsigned int iteratorSize() const = 0;
```

## Return Value

The size in bytes of the iteration context needed by the subclass of OSCollection.

## Overview

This pure virtual member function, which subclasses must implement, is called by an OSCollectionIterator object so that it can allocate the storage needed for the iteration context. An iteration context contains the data necessary to iterate through the collection.

## See Also

### Miscellaneous
- [copyCollection](./api-1808206-copycollection.md)
  Creates a deep copy of a collection.
- [ensureCapacity](./api-1808212-ensurecapacity.md)
  Ensures the collection has enough space to store the requested number of objects.
- [flushCollection](./api-1808219-flushcollection.md)
  Empties the collection, releasing any objects retained.
- [getCapacity](./api-1808225-getcapacity.md)
  Returns the number of objects the collection can store without reallocating.
- [getCapacityIncrement](./api-1808233-getcapacityincrement.md)
  Returns the storage increment of the collection.
- [getCount](./api-1808238-getcount.md)
  Returns the number of objects in the collection.
- [getNextObjectForIterator](./api-1808244-getnextobjectforiterator.md)
  Returns the next member of a collection.
- [haveUpdated](./api-1808248-haveupdated.md)
  Tracks updates to the collection.
- [init](./api-1808252-init.md)
  Initializes the OSCollection object.
- [initIterator](./api-1808258-inititerator.md)
  Initializes the iteration context for a collection subclass.
- [setCapacityIncrement](./api-1808267-setcapacityincrement.md)
  Sets the storage increment of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollection/1808262-iteratorsize)*