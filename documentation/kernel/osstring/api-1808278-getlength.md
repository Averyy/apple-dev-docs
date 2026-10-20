# getLength

**Framework**: Kernel  
**Kind**: instm

Returns the number of characters in the OSString object.

## Declaration

```cpp
virtual unsigned int getLength() const;
```

#### Return Value

The number of characters in the OSString object.

## See Also

### Miscellaneous
- [free](./api-1808271-free.md)
  Deallocates or releases any resources used by the OSString instance.
- [getChar](./api-1808273-getchar.md)
  Returns the character at a given index in the string object.
- [getCStringNoCopy](./api-1808275-getcstringnocopy.md)
  Returns a pointer to the internal C string buffer.
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
- [withString](./api-1808306-withstring.md)
  Creates and initializes an OSString from another OSString.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/1808278-getlength)*