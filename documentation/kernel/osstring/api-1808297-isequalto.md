# isEqualTo(const OSString *)

**Framework**: Kernel  
**Kind**: instm

Tests the equality of two OSString objects.

## Declaration

```swift
virtual bool isEqualTo(
 const OSString *aString) const;
```

#### Return_value

`true` if the two OSString objects are equivalent, `false` otherwise.

#### Overview

Two OSString objects are considered equal if they have same length and if their byte buffers hold the same contents.

## Parameters

- `aString`: The OSString object being compared against the receiver.

## See Also

- [free](osstring/1808271-free.md)
  Deallocates or releases any resources used by the OSString instance.
- [getChar](osstring/1808273-getchar.md)
  Returns the character at a given index in the string object.
- [getCStringNoCopy](osstring/1808275-getcstringnocopy.md)
  Returns a pointer to the internal C string buffer.
- [getLength](osstring/1808278-getlength.md)
  Returns the number of characters in the OSString object.
- [initWithCString](osstring/1808281-initwithcstring.md)
  Initializes an OSString from a C string.
- [initWithCStringNoCopy](osstring/1808284-initwithcstringnocopy.md)
  Initializes an immutable OSString to share the provided C string buffer.
- [initWithString](osstring/1808286-initwithstring.md)
  Initializes an OSString from another OSString.
- [isEqualTo(const char *)](osstring/1808288-isequalto.md)
  Tests the equality of an OSString object with a C string.
- [isEqualTo(const OSData *)](osstring/1808292-isequalto.md)
  Tests the equality of an OSData object and the OSString instance.
- [isEqualTo(const OSMetaClassBase *)](osstring/1808295-isequalto.md)
  Tests the equality of an OSString object to an arbitrary object.
- [serialize](osstring/1808298-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setChar](osstring/1808300-setchar.md)
  Replaces a character at a given index in the string object.
- [withCString](osstring/1808301-withcstring.md)
  Creates and initializes an OSString from a C string.
- [withCStringNoCopy](osstring/1808304-withcstringnocopy.md)
  Creates and initializes an immutable OSString that shares the provided C string buffer.
- [withString](osstring/1808306-withstring.md)
  Creates and initializes an OSString from another OSString.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/1808297-isequalto)*