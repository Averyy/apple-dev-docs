# isEqualTo(const OSMetaClassBase *)

**Framework**: Kernel  
**Kind**: instm

Tests the equality an OSNumber to an arbitrary object.

## Declaration

```cpp
virtual bool isEqualTo(
 const OSMetaClassBase *anObject) const;
```

#### Return Value

`true` if the objects are equal, `false` if not.

#### Overview

An OSNumber is considered equal to another object if that object is derived from OSNumber and represents the same C integer value.

## Parameters

- `anObject`: An object to be compared against the receiver.

## See Also

### Miscellaneous
- [addValue](./api-1808041-addvalue.md)
  Adds a signed integer value to the internal integer value of the OSNumber object.
- [free](./api-1808049-free.md)
  Deallocates or releases any resources used by the OSNumber instance.
- [init(const char *, unsigned int)](./api-1808057-init.md)
  Initializes an instance of OSNumber with an unsigned integer value represented as a C string.
- [init(unsigned long long, unsigned int)](./api-1808065-init.md)
  Initializes an instance of OSNumber with an integer value.
- [isEqualTo(const OSNumber *)](./api-1808076-isequalto.md)
  Tests the equality of two OSNumber objects.
- [numberOfBits](./api-1808083-numberofbits.md)
  Returns the number of bits used to represent the OSNumber object's integer value.
- [numberOfBytes](./api-1808091-numberofbytes.md)
  Returns the number of bytes used to represent the OSNumber object's integer value.
- [serialize](./api-1808097-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setValue](./api-1808102-setvalue.md)
  Replaces the current internal integer value of the OSNumber object by the value given.
- [unsigned16BitValue](./api-1808108-unsigned16bitvalue.md)
  Returns the OSNumber object's integer value cast as an unsigned 16-bit integer.
- [unsigned32BitValue](./api-1808115-unsigned32bitvalue.md)
  Returns the OSNumber object's integer value cast as an unsigned 32-bit integer.
- [unsigned64BitValue](./api-1808123-unsigned64bitvalue.md)
  Returns the OSNumber object's integer value cast as an unsigned 64-bit integer.
- [unsigned8BitValue](./api-1808129-unsigned8bitvalue.md)
  Returns the OSNumber object's integer value cast as an unsigned 8-bit integer.
- [withNumber(const char *, unsigned int)](./api-1808136-withnumber.md)
  Creates and initializes an instance of OSNumber with an unsigned integer value represented as a C string.
- [withNumber(unsigned long long, unsigned int)](./api-1808143-withnumber.md)
  Creates and initializes an instance of OSNumber with an integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osnumber/1808071-isequalto)*