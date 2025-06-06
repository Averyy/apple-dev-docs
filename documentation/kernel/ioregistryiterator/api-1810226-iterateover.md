# iterateOver(const IORegistryPlane *, IOOptionBits)

**Framework**: Kernel  
**Kind**: instm

Create an iterator rooted at the registry root.

## Declaration

```swift
static IORegistryIterator * iterateOver(
 const IORegistryPlane *plane, 
 IOOptionBits options = 0 );
```

#### Return_value

A created IORegistryIterator instance, to be released by the caller when it has finished with it.

#### Overview

This method creates an IORegistryIterator that is set up with options to iterate children of the registry root entry, and to recurse automatically into entries as they are returned, or only when instructed. The iterator object keeps track of entries that have been recursed into previously to avoid loops.

## Parameters

- `plane`: A plane object must be specified.
- `options`: kIORegistryIterateRecursively may be set to recurse automatically into each entry as it is returned. This option affects the behaviour of the getNextObject method, which is defined in the OSIterator superclass. Other methods will override this behaviour. kIORegistryIterateParents may be set to iterate the parents of each entry, by default the children are iterated.

## See Also

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
- [iterateOver(IORegistryEntry *, const IORegistryPlane *, IOOptionBits)](ioregistryiterator/1810260-iterateover.md)
  Create an iterator rooted at a given registry entry.
- [reset](ioregistryiterator/1810295-reset.md)
  Exits all levels of recursion, restoring the iterator to its state at creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioregistryiterator/1810226-iterateover)*