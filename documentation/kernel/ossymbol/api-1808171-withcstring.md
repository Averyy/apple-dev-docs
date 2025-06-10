# withCString

**Framework**: Kernel  
**Kind**: instm

Returns an OSSymbol created from a C string, or the existing unique instance of the same value.

## Declaration

```swift
static const OSSymbol * withCString(
 const char *cString);
```

#### Return_value

An instance of OSSymbol representing the same characters as `cString`; `NULL` on failure.

#### Overview

This function returns the unique OSSymbol instance representing the string value of `cString`. You can compare it with other OSSymbols using the `==` operator.

OSSymbols are reference-counted normally. This function either returns a new OSSymbol with a retain count of 1, or increments the retain count of the existing instance.

## Parameters

- `cString`: The C string to look up or copy.

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
- [isEqualTo(const char *)](ossymbol/1808093-isequalto.md)
  Tests the equality of an OSSymbol object with a C string.
- [isEqualTo(const OSSymbol *)](ossymbol/1808114-isequalto.md)
  Tests the equality of two OSSymbol objects.
- [taggedRelease(const void *)](ossymbol/1808137-taggedrelease.md)
  Overrides OSObject::taggedRelease(const void *) to synchronize with the symbol pool.
- [taggedRelease(const void *, const int)](ossymbol/1808154-taggedrelease.md)
  Overrides OSObject::taggedRelease(const void *, const int) to synchronize with the symbol pool.
- [withCStringNoCopy](ossymbol/1808179-withcstringnocopy.md)
  Returns an OSSymbol created from a C string, without copying that string, or the existing unique instance of the same value.
- [withString](ossymbol/1808192-withstring.md)
  Returns an OSSymbol created from an OSString, or the existing unique instance of the same value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ossymbol/1808171-withcstring)*