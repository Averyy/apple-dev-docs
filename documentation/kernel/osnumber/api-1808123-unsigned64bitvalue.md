# unsigned64BitValue

**Framework**: Kernel  
**Kind**: instm

Returns the OSNumber object's integer value cast as an unsigned 64-bit integer.

## Declaration

```swift
virtual unsigned long long unsigned64BitValue() const;
```

#### Return_value

Returns the OSNumber object's integer value cast as an unsigned 64-bit integer.

#### Overview

This function merely casts the internal integer value, giving no indication of truncation or other potential conversion problems.

## See Also

- [addValue](osnumber/1808041-addvalue.md)
  Adds a signed integer value to the internal integer value of the OSNumber object.
- [free](osnumber/1808049-free.md)
  Deallocates or releases any resources used by the OSNumber instance.
- [init(const char *, unsigned int)](osnumber/1808057-init.md)
  Initializes an instance of OSNumber with an unsigned integer value represented as a C string.
- [init(unsigned long long, unsigned int)](osnumber/1808065-init.md)
  Initializes an instance of OSNumber with an integer value.
- [isEqualTo(const OSMetaClassBase *)](osnumber/1808071-isequalto.md)
  Tests the equality an OSNumber to an arbitrary object.
- [isEqualTo(const OSNumber *)](osnumber/1808076-isequalto.md)
  Tests the equality of two OSNumber objects.
- [numberOfBits](osnumber/1808083-numberofbits.md)
  Returns the number of bits used to represent the OSNumber object's integer value.
- [numberOfBytes](osnumber/1808091-numberofbytes.md)
  Returns the number of bytes used to represent the OSNumber object's integer value.
- [serialize](osnumber/1808097-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setValue](osnumber/1808102-setvalue.md)
  Replaces the current internal integer value of the OSNumber object by the value given.
- [unsigned16BitValue](osnumber/1808108-unsigned16bitvalue.md)
  Returns the OSNumber object's integer value cast as an unsigned 16-bit integer.
- [unsigned32BitValue](osnumber/1808115-unsigned32bitvalue.md)
  Returns the OSNumber object's integer value cast as an unsigned 32-bit integer.
- [unsigned8BitValue](osnumber/1808129-unsigned8bitvalue.md)
  Returns the OSNumber object's integer value cast as an unsigned 8-bit integer.
- [withNumber(const char *, unsigned int)](osnumber/1808136-withnumber.md)
  Creates and initializes an instance of OSNumber with an unsigned integer value represented as a C string.
- [withNumber(unsigned long long, unsigned int)](osnumber/1808143-withnumber.md)
  Creates and initializes an instance of OSNumber with an integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osnumber/1808123-unsigned64bitvalue)*