# isValid

**Framework**: Kernel  
**Kind**: instm

Checks that no registry changes have invalidated the iteration.

## Declaration

```swift
virtual bool isValid(
 void );
```

#### Return_value

false if the iterator has been invalidated by changes to the registry, true otherwise.

#### Overview

If a registry iteration is invalidated by changes to the registry, it will be made invalid, the currentEntry will be considered zero, and further calls to getNextObject et al. will return zero. The iterator should be reset to restart the iteration when this happens.

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
- [iterateAll](ioregistryiterator/1810202-iterateall.md)
  Iterates all entries (with getNextObject) and returns a set of all returned entries.
- [iterateOver(const IORegistryPlane *, IOOptionBits)](ioregistryiterator/1810226-iterateover.md)
  Create an iterator rooted at the registry root.
- [iterateOver(IORegistryEntry *, const IORegistryPlane *, IOOptionBits)](ioregistryiterator/1810260-iterateover.md)
  Create an iterator rooted at a given registry entry.
- [reset](ioregistryiterator/1810295-reset.md)
  Exits all levels of recursion, restoring the iterator to its state at creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioregistryiterator/1810181-isvalid)*