# isEqualTo(const char *)

**Framework**: Kernel  
**Kind**: instm

Tests the equality of an OSSymbol object with a C string.

## Declaration

```swift
virtual bool isEqualTo(
 const char *cString) const;
```

#### Return_value

`true` if the OSSymbol's characters are equivalent to the C string's, `false` otherwise.

## Parameters

- `cString`: The C string to compare against the receiver.

## See Also

- [free](ossymbol/1808021-free.md)
  Overrides OSObject::free to synchronize with the symbol pool.
- [initWithCString](ossymbol/1808026-initwithcstring.md)
  Overridden to prevent creation of duplicate symbols.
- [initWithCStringNoCopy](ossymbol/1808036-initwithcstringnocopy.md)
  Overridden to prevent creation of duplicate symbols.
- [initWithString](ossymbol/1808054-initwithstring.md)
  Overridden to prevent creation of duplicate symbols.
- [isEqualTo](ossymbol/1808078-isequalto.md)
  Tests the equality of an OSSymbol object to an arbitrary object.
- [isEqualTo(const OSSymbol *)](ossymbol/1808114-isequalto.md)
  Tests the equality of two OSSymbol objects.
- [taggedRelease(const void *)](ossymbol/1808137-taggedrelease.md)
  Overrides OSObject::taggedRelease(const void *) to synchronize with the symbol pool.
- [taggedRelease(const void *, const int)](ossymbol/1808154-taggedrelease.md)
  Overrides OSObject::taggedRelease(const void *, const int) to synchronize with the symbol pool.
- [withCString](ossymbol/1808171-withcstring.md)
  Returns an OSSymbol created from a C string, or the existing unique instance of the same value.
- [withCStringNoCopy](ossymbol/1808179-withcstringnocopy.md)
  Returns an OSSymbol created from a C string, without copying that string, or the existing unique instance of the same value.
- [withString](ossymbol/1808192-withstring.md)
  Returns an OSSymbol created from an OSString, or the existing unique instance of the same value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ossymbol/1808093-isequalto)*