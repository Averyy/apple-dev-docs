# withString

**Framework**: Kernel  
**Kind**: instm

Creates and initializes an OSString from another OSString.

## Declaration

```c
static OSString * withString(
 const OSString *aString);
```

## Return Value

An instance of OSString representing the same characters as `aString`, and with a reference count of 1; `NULL` on failure.

## Overview

The new OSString is a distinct instance from `aString`, and is not merely the original object with the reference count incremented. Changes to one will not be reflected in the other.

## Parameters

- `aString`: The OSString object whose contents to copy.

## See Also

### Miscellaneous
- [free](./api-1808271-free.md)
  Deallocates or releases any resources used by the OSString instance.
- [getChar](./api-1808273-getchar.md)
  Returns the character at a given index in the string object.
- [getCStringNoCopy](./api-1808275-getcstringnocopy.md)
  Returns a pointer to the internal C string buffer.
- [getLength](./api-1808278-getlength.md)
  Returns the number of characters in the OSString object.
- [initWithCString](./api-1808281-initwithcstring.md)
  Initializes an OSString from a C string.
- [initWithCStringNoCopy](./api-1808284-initwithcstringnocopy.md)
  Initializes an immutable OSString to share the provided C string buffer.
- [initWithString](./api-1808286-initwithstring.md)
  Initializes an OSString from another OSString.
- [isEqualTo(const char *)](./api-1808288-isequalto.md)
  Tests the equality of an OSString object with a C string.
- [isEqualTo(const OSData *)](./api-1808292-isequalto.md)
  Tests the equality of an OSData object and the OSString instance.
- [isEqualTo(const OSMetaClassBase *)](./api-1808295-isequalto.md)
  Tests the equality of an OSString object to an arbitrary object.
- [isEqualTo(const OSString *)](./api-1808297-isequalto.md)
  Tests the equality of two OSString objects.
- [serialize](./api-1808298-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setChar](./api-1808300-setchar.md)
  Replaces a character at a given index in the string object.
- [withCString](./api-1808301-withcstring.md)
  Creates and initializes an OSString from a C string.
- [withCStringNoCopy](./api-1808304-withcstringnocopy.md)
  Creates and initializes an immutable OSString that shares the provided C string buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/1808306-withstring)*