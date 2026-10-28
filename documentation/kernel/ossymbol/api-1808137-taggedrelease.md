# taggedRelease(const void *)

**Framework**: Kernel  
**Kind**: instm

Overrides OSObject::taggedRelease(const void *) to synchronize with the symbol pool.

## Declaration

```cpp
virtual void taggedRelease(
 const void *tag) const;
```

## Overview

Because OSSymbol shares instances, the reference-counting functions must synchronize access to the class-internal tables used to track those instances.

## Parameters

- `tag`: Used for tracking collection references.

## See Also

### Miscellaneous
- [free](./api-1808021-free.md)
  Overrides OSObject::free to synchronize with the symbol pool.
- [initWithCString](./api-1808026-initwithcstring.md)
  Overridden to prevent creation of duplicate symbols.
- [initWithCStringNoCopy](./api-1808036-initwithcstringnocopy.md)
  Overridden to prevent creation of duplicate symbols.
- [initWithString](./api-1808054-initwithstring.md)
  Overridden to prevent creation of duplicate symbols.
- [isEqualTo](./api-1808078-isequalto.md)
  Tests the equality of an OSSymbol object to an arbitrary object.
- [isEqualTo(const char *)](./api-1808093-isequalto.md)
  Tests the equality of an OSSymbol object with a C string.
- [isEqualTo(const OSSymbol *)](./api-1808114-isequalto.md)
  Tests the equality of two OSSymbol objects.
- [taggedRelease(const void *, const int)](./api-1808154-taggedrelease.md)
  Overrides OSObject::taggedRelease(const void *, const int) to synchronize with the symbol pool.
- [withCString](./api-1808171-withcstring.md)
  Returns an OSSymbol created from a C string, or the existing unique instance of the same value.
- [withCStringNoCopy](./api-1808179-withcstringnocopy.md)
  Returns an OSSymbol created from a C string, without copying that string, or the existing unique instance of the same value.
- [withString](./api-1808192-withstring.md)
  Returns an OSSymbol created from an OSString, or the existing unique instance of the same value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ossymbol/1808137-taggedrelease)*