# OSCollectionIterator

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSCollectionIterator : OSIterator
```

#### Overview

OSCollectionIterator defines a consistent mechanism to iterate through the objects of an OSCollection. It expands on the basic interface of OSIterator to allow association of an iterator with a specific collection.

To use an OSCollectionIterator, you create it with the collection to be iterated, then call OSIterator as long as it returns an object:

<pre> OSCollectionIterator * iterator = OSCollectionIterator::withCollection(myCollection); OSObject * object; while (object = iterator->getNextObject()) { // do something with object } // optional if (!iterator->isValid()) { // report that collection changed during iteration } iterator->release(); </pre>

Note that when iterating associative collections, the objects returned by `getNextObject` are keys; if you want to work with the associated values, simply look them up in the collection with the keys.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSCollectionIterator provides no concurrency protection.

## Topics

### Miscellaneous
- [free](oscollectioniterator/1808113-free.md)
  Releases or deallocates any resources used by the OSCollectionIterator object.
- [getNextObject](oscollectioniterator/1808125-getnextobject.md)
  Advances to and returns the next object in the iteration.
- [initWithCollection](oscollectioniterator/1808147-initwithcollection.md)
  Initializes an OSCollectionIterator for the provided collection object.
- [isValid](oscollectioniterator/1808157-isvalid.md)
  Checks that the collection hasn't been modified during iteration.
- [reset](oscollectioniterator/1808170-reset.md)
  Resets the iterator to the beginning of the collection, as if it had just been created.
- [withCollection](oscollectioniterator/1808183-withcollection.md)
  Creates and initializes an OSCollectionIterator for the provided collection object.
### Instance Methods
- [- free](oscollectioniterator/1542649-free.md)
- [- getMetaClass](oscollectioniterator/1542654-getmetaclass.md)
- [- getNextObject](oscollectioniterator/1542659-getnextobject.md)
- [- initWithCollection](oscollectioniterator/1542661-initwithcollection.md)
- [- isValid](oscollectioniterator/1542655-isvalid.md)
- [- reset](oscollectioniterator/1542652-reset.md)
### Type Methods
- [+ withCollection](oscollectioniterator/1542657-withcollection.md)

## Relationships

### Inherits From
- [OSIterator](ositerator.md)

## See Also

- [OSArray](osarray.md)
  OSArray provides an indexed store of objects.
- [OSDictionary](osdictionary.md)
  OSDictionary provides an associative store using strings for keys.
- [OSSet](osset.md)
  OSSet provides an unordered set store of objects.
- [OSOrderedSet](osorderedset.md)
  OSOrderedSet provides an ordered set store of objects.
- [OSCollection](oscollection.md)
  The abstract superclass for Libkern collections.
- [OSIterator](ositerator.md)
  The abstract superclass for Libkern iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollectioniterator)*