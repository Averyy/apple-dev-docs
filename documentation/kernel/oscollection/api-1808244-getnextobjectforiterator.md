# getNextObjectForIterator

**Framework**: Kernel  
**Kind**: instm

Returns the next member of a collection.

## Declaration

```swift
virtual bool getNextObjectForIterator( 
 void *iterationContext, 
 OSObject **nextObject) const = 0;
```

#### Return_value

`true` if an object was found, `false` otherwise.

#### Overview

This pure virtual member function, which subclasses must implement, is called by an OSCollectionIterator to get the next object for a given iteration context. The collection object should interpret `iterationContext` appropriately, advance the context from its current object to the next object (if it exists), return that object by reference in `nextObject`, and return `true` for the function call. If there is no next object, the collection object must return `false`.

For associative collections, the object returned should be the key used to access its associated value, and not the value itself.

## Parameters

- `iterationContext`: The iteration context.
- `nextObject`: The object returned by reference to the caller.

## See Also

- [copyCollection](oscollection/1808206-copycollection.md)
  Creates a deep copy of a collection.
- [ensureCapacity](oscollection/1808212-ensurecapacity.md)
  Ensures the collection has enough space to store the requested number of objects.
- [flushCollection](oscollection/1808219-flushcollection.md)
  Empties the collection, releasing any objects retained.
- [getCapacity](oscollection/1808225-getcapacity.md)
  Returns the number of objects the collection can store without reallocating.
- [getCapacityIncrement](oscollection/1808233-getcapacityincrement.md)
  Returns the storage increment of the collection.
- [getCount](oscollection/1808238-getcount.md)
  Returns the number of objects in the collection.
- [haveUpdated](oscollection/1808248-haveupdated.md)
  Tracks updates to the collection.
- [init](oscollection/1808252-init.md)
  Initializes the OSCollection object.
- [initIterator](oscollection/1808258-inititerator.md)
  Initializes the iteration context for a collection subclass.
- [iteratorSize](oscollection/1808262-iteratorsize.md)
  Returns the size in bytes of a subclass's iteration context.
- [setCapacityIncrement](oscollection/1808267-setcapacityincrement.md)
  Sets the storage increment of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollection/1808244-getnextobjectforiterator)*