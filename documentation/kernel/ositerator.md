# OSIterator

**Framework**: Kernel  
**Kind**: cl

The abstract superclass for Libkern iterators.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSIterator : OSObject
```

#### Overview

OSIterator is the abstract superclass for all Libkern C++ object iterators. It defines the basic interface for iterating and resetting. See OSCollection and OSCollectionIterator for more information.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSIterator provides no concurrency protection.

## Topics

### Miscellaneous
- [getNextObject](ositerator/1808048-getnextobject.md)
  Advances to and returns the next object in the iteration.
- [isValid](ositerator/1808063-isvalid.md)
  Check that the collection hasn't been modified during iteration.
- [reset](ositerator/1808074-reset.md)
  Resets the iterator to the beginning of the collection, as if it had just been created.
### Instance Methods
- [- getMetaClass](ositerator/1416195-getmetaclass.md)
- [- getNextObject](ositerator/1416192-getnextobject.md)
- [- isValid](ositerator/1416199-isvalid.md)
- [- reset](ositerator/1416194-reset.md)

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
- [OSCollection](oscollection.md)
  The abstract superclass for Libkern collections.
- [OSCollectionIterator](oscollectioniterator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ositerator)*