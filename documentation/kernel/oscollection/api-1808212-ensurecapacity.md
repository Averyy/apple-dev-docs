# ensureCapacity

**Framework**: Kernel  
**Kind**: instm

Ensures the collection has enough space to store the requested number of objects.

## Declaration

```cpp
virtual unsigned int ensureCapacity(
 unsigned intnewCapacity) = 0;
```

## Return Value

The new capacity of the collection, which may be different from the number requested (if smaller, reallocation of storage failed).

## Overview

Subclasses implement this pure virtual member function to adjust their storage so that they can hold at least `newCapacity` objects. Libkern collections generally allocate storage in multiples of their capacity increment.

Subclass methods that add objects to the collection should call this function before adding any object, and should check the return value for success.

Collection subclasses may reduce their storage when the number of contained objects falls below some threshold, but no Libkern collections currently do.

## Parameters

- `newCapacity`: The total number of objects the collection should be able to store.

## See Also

### Miscellaneous
- [copyCollection](./api-1808206-copycollection.md)
  Creates a deep copy of a collection.
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
- [iteratorSize](./api-1808262-iteratorsize.md)
  Returns the size in bytes of a subclass's iteration context.
- [setCapacityIncrement](./api-1808267-setcapacityincrement.md)
  Sets the storage increment of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollection/1808212-ensurecapacity)*