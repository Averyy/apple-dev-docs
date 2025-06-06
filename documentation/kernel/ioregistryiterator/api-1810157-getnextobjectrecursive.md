# getNextObjectRecursive

**Framework**: Kernel  
**Kind**: instm

Return the next object in the registry iteration, and enter it.

## Declaration

```swift
virtual IORegistryEntry * getNextObjectRecursive(
 void );
```

#### Return_value

The next registry entry in the iteration (the current entry), or zero if its finished, or the iteration is invalid (see isValid). The entry returned is retained while the iterator is pointing at it (its the current entry), or recursing into it. The caller should not release it.

#### Overview

If the iterator has a current entry, and the iterator has not already entered previously, enterEntry is called to recurse into it, ie. make it the new root, and the next child, or parent if the kIORegistryIterateParents option was used to create the iterator, at this new level of recursion is returned. If there is no current entry at this level of recursion, exitEntry is called and the process repeats, until the iteration returns to the entry the iterator was created with and zero is returned. The object returned is retained while the iterator is pointing at it (its the current entry), or recursing into it. The caller should not release it.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioregistryiterator/1810157-getnextobjectrecursive)*