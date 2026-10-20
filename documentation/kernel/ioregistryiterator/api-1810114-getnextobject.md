# getNextObject

**Framework**: Kernel  
**Kind**: instm

Return the next object in the registry iteration.

## Declaration

```cpp
virtual IORegistryEntry * getNextObject(
 void );
```

#### Return Value

The next registry entry in the iteration (the current entry), or zero if the iteration has finished at this level of recursion. The entry returned is retained while the iterator is pointing at it (its the current entry), or recursing into it. The caller should not release it.

#### Overview

This method calls either getNextObjectFlat or getNextObjectRecursive depending on the options the iterator was created with. This implements the OSIterator defined getNextObject method. The object returned is retained while the iterator is pointing at it (its the current entry), or recursing into it. The caller should not release it.

## See Also

### Miscellaneous
- [enterEntry()](./api-1810048-enterentry.md)
  Recurse into the current entry in the registry iteration.
- [enterEntry(const IORegistryPlane *)](./api-1810063-enterentry.md)
  Recurse into the current entry in the registry iteration.
- [exitEntry](./api-1810081-exitentry.md)
  Exits a level of recursion, restoring the current entry.
- [getCurrentEntry](./api-1810099-getcurrententry.md)
  Return the current entry in the registry iteration.
- [getNextObjectFlat](./api-1810135-getnextobjectflat.md)
  Return the next object in the registry iteration, ignoring the kIORegistryIterateRecursively option.
- [getNextObjectRecursive](./api-1810157-getnextobjectrecursive.md)
  Return the next object in the registry iteration, and enter it.
- [isValid](./api-1810181-isvalid.md)
  Checks that no registry changes have invalidated the iteration.
- [iterateAll](./api-1810202-iterateall.md)
  Iterates all entries (with getNextObject) and returns a set of all returned entries.
- [iterateOver(const IORegistryPlane *, IOOptionBits)](./api-1810226-iterateover.md)
  Create an iterator rooted at the registry root.
- [iterateOver(IORegistryEntry *, const IORegistryPlane *, IOOptionBits)](./api-1810260-iterateover.md)
  Create an iterator rooted at a given registry entry.
- [reset](./api-1810295-reset.md)
  Exits all levels of recursion, restoring the iterator to its state at creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioregistryiterator/1810114-getnextobject)*