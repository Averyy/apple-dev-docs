# isEqualTo

**Framework**: Kernel  
**Kind**: instm

Tests the equality of an OSSymbol object to an arbitrary object.

## Declaration

```cpp
virtual bool isEqualTo(
 const OSMetaClassBase *anObject) const;
```

## Return Value

Returns `true` if the two objects are equivalent, `false` otherwise.

## Overview

An OSSymbol is considered equal to another object if that object is derived from OSString and contains the equivalent bytes of the same length.

## Parameters

- `anObject`: The object to be compared against the receiver.

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
- [isEqualTo(const char *)](./api-1808093-isequalto.md)
  Tests the equality of an OSSymbol object with a C string.
- [isEqualTo(const OSSymbol *)](./api-1808114-isequalto.md)
  Tests the equality of two OSSymbol objects.
- [taggedRelease(const void *)](./api-1808137-taggedrelease.md)
  Overrides OSObject::taggedRelease(const void *) to synchronize with the symbol pool.
- [taggedRelease(const void *, const int)](./api-1808154-taggedrelease.md)
  Overrides OSObject::taggedRelease(const void *, const int) to synchronize with the symbol pool.
- [withCString](./api-1808171-withcstring.md)
  Returns an OSSymbol created from a C string, or the existing unique instance of the same value.
- [withCStringNoCopy](./api-1808179-withcstringnocopy.md)
  Returns an OSSymbol created from a C string, without copying that string, or the existing unique instance of the same value.
- [withString](./api-1808192-withstring.md)
  Returns an OSSymbol created from an OSString, or the existing unique instance of the same value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ossymbol/1808078-isequalto)*