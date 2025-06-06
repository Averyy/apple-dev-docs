# IORegistryIterator

**Framework**: Kernel  
**Kind**: cl

An iterator over the registry.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef struct IORegistryIterator IORegistryIterator;
```

#### Overview

An iterator that can traverse the children or parents of a registry entry in a plane, and recurse. Access to the registry is protected against multiple threads, but an IORegistryIterator instance is for use by one thread only.

## Topics

### Miscellaneous
- [enterEntry()](ioregistryiterator/1810048-enterentry.md)
  Recurse into the current entry in the registry iteration.
- [enterEntry(const IORegistryPlane *)](ioregistryiterator/1810063-enterentry.md)
  Recurse into the current entry in the registry iteration.
- [exitEntry](ioregistryiterator/1810081-exitentry.md)
  Exits a level of recursion, restoring the current entry.
- [getCurrentEntry](ioregistryiterator/1810099-getcurrententry.md)
  Return the current entry in the registry iteration.
- [getNextObject](ioregistryiterator/1810114-getnextobject.md)
  Return the next object in the registry iteration.
- [getNextObjectFlat](ioregistryiterator/1810135-getnextobjectflat.md)
  Return the next object in the registry iteration, ignoring the kIORegistryIterateRecursively option.
- [getNextObjectRecursive](ioregistryiterator/1810157-getnextobjectrecursive.md)
  Return the next object in the registry iteration, and enter it.
- [isValid](ioregistryiterator/1810181-isvalid.md)
  Checks that no registry changes have invalidated the iteration.
- [iterateAll](ioregistryiterator/1810202-iterateall.md)
  Iterates all entries (with getNextObject) and returns a set of all returned entries.
- [iterateOver(const IORegistryPlane *, IOOptionBits)](ioregistryiterator/1810226-iterateover.md)
  Create an iterator rooted at the registry root.
- [iterateOver(IORegistryEntry *, const IORegistryPlane *, IOOptionBits)](ioregistryiterator/1810260-iterateover.md)
  Create an iterator rooted at a given registry entry.
- [reset](ioregistryiterator/1810295-reset.md)
  Exits all levels of recursion, restoring the iterator to its state at creation.
### Instance Methods
- [- enterEntry](ioregistryiterator/1437673-enterentry.md)
- [- enterEntry](ioregistryiterator/3516480-enterentry.md)
- [- exitEntry](ioregistryiterator/1437616-exitentry.md)
- [- free](ioregistryiterator/1437743-free.md)
- [- getCurrentEntry](ioregistryiterator/1437723-getcurrententry.md)
- [- getMetaClass](ioregistryiterator/1437730-getmetaclass.md)
- [- getNextObject](ioregistryiterator/1437629-getnextobject.md)
- [- getNextObjectFlat](ioregistryiterator/1437684-getnextobjectflat.md)
- [- getNextObjectRecursive](ioregistryiterator/1437739-getnextobjectrecursive.md)
- [- isValid](ioregistryiterator/1437675-isvalid.md)
- [- iterateAll](ioregistryiterator/1437708-iterateall.md)
- [- reset](ioregistryiterator/1437700-reset.md)
### Type Methods
- [+ iterateOver](ioregistryiterator/1437636-iterateover.md)
- [+ iterateOver](ioregistryiterator/3516481-iterateover.md)

## Relationships

### Inherits From
- [OSIterator](ositerator.md)

## See Also

- [IORegistryEntry](ioregistryentry.md)
  The base class for all objects in the registry.
- [IOBSDNameMatching](1575336-iobsdnamematching.md)
  Create a matching dictionary that specifies an IOService match based on BSD device name.
- [IOPrintPlane](1558295-ioprintplane.md)
- [Registry Utilities](iokit_fundamentals/registry_utilities.md)
- [Registry Keys](iokit_fundamentals/registry_keys.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioregistryiterator)*