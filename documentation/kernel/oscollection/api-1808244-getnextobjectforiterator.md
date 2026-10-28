# getNextObjectForIterator

**Framework**: Kernel  
**Kind**: instm

Returns the next member of a collection.

## Declaration

```cpp
virtual bool getNextObjectForIterator( 
 void *iterationContext, 
 OSObject **nextObject) const = 0;
```

## Return Value

`true` if an object was found, `false` otherwise.

## Overview

This pure virtual member function, which subclasses must implement, is called by an OSCollectionIterator to get the next object for a given iteration context. The collection object should interpret `iterationContext` appropriately, advance the context from its current object to the next object (if it exists), return that object by reference in `nextObject`, and return `true` for the function call. If there is no next object, the collection object must return `false`.

For associative collections, the object returned should be the key used to access its associated value, and not the value itself.

## Parameters

- `iterationContext`: The iteration context.
- `nextObject`: The object returned by reference to the caller.

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
- [haveUpdated](./api-1808248-haveupdated.md)
  Tracks updates to the collection.
- [init](./api-1808252-init.md)
  Initializes the OSCollection object.
- [initIterator](./api-1808258-inititerator.md)
  Initializes the iteration context for a collection subclass.
- [iteratorSize](./api-1808262-iteratorsize.md)
  Returns the size in bytes of a subclass's iteration context.
- [setCapacityIncrement](./api-1808267-setcapacityincrement.md)
  Sets the storage increment of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollection/1808244-getnextobjectforiterator)*