# OSCollection

**Framework**: Kernel  
**Kind**: cl

The abstract superclass for Libkern collections.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSCollection : OSObject
```

#### Overview

OSCollection is the abstract superclass for all Libkern C++ object collections. It defines the necessary interfaces for managing storage space and iterating through an arbitrary collection (see the OSIterator and OSCollectionIterator classes). It is up to concrete subclasses to define their specific content management functions.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSCollection provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
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
- [getNextObjectForIterator](oscollection/1808244-getnextobjectforiterator.md)
  Returns the next member of a collection.
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
### DataTypes
- [_OSCollectionFlags](oscollection/oscollectionflags.md)
### Instance Methods
- [- copyCollection](oscollection/1569367-copycollection.md)
- [- ensureCapacity](../driverkit/oscollection/ensurecapacity.md)
- [- flushCollection](../driverkit/oscollection/flushcollection.md)
- [- getCapacity](../driverkit/oscollection/getcapacity.md)
- [- getCapacityIncrement](oscollection/1569369-getcapacityincrement.md)
- [- getCount](../driverkit/oscollection/getcount.md)
- [- getMetaClass](oscollection/1569378-getmetaclass.md)
- [- getNextObjectForIterator](oscollection/1569375-getnextobjectforiterator.md)
- [- haveUpdated](oscollection/1569376-haveupdated.md)
- [- init](oscollection/1569374-init.md)
- [- initIterator](oscollection/1569368-inititerator.md)
- [- iterateObjects](oscollection/2967351-iterateobjects.md)
- [- iterateObjects](oscollection/3516833-iterateobjects.md)
- [- iteratorSize](oscollection/1569370-iteratorsize.md)
- [- setCapacityIncrement](oscollection/1569371-setcapacityincrement.md)
- [- setOptions](oscollection/1569373-setoptions.md)
  Recursively sets option bits in this collection and all child collections.

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [OSArray](osarray.md)
  OSArray provides an indexed store of objects.
- [OSDictionary](osdictionary.md)
  OSDictionary provides an associative store using strings for keys.
- [OSSet](osset.md)
  OSSet provides an unordered set store of objects.
- [OSOrderedSet](osorderedset.md)
  OSOrderedSet provides an ordered set store of objects.
- [OSCollectionIterator](oscollectioniterator.md)
- [OSIterator](ositerator.md)
  The abstract superclass for Libkern iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/oscollection)*