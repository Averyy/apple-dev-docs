# withNumber(const char *, unsigned int)

**Framework**: Kernel  
**Kind**: instm

Creates and initializes an instance of OSNumber with an unsigned integer value represented as a C string.

## Declaration

```swift
static OSNumber * withNumber( 
 const char *valueString, 
 unsigned intnumberOfBits);
```

#### Return_value

An instance of OSNumber with a reference count of 1; `NULL` on failure.

#### Overview

This function does not work in I/O Kit versions prior to 8.0 (OS X 10.4). In I/O Kit version 8.0 and later, it works but is limited to parsing unsigned 32 bit quantities. The format of the C string may be decimal, hexadecimal ("0x" prefix), binary ("0b" prefix), or octal ("0" prefix).

The parsed value is masked to the provided `numberOfBits` when the OSNumber object is initialized.

You can change the value of an OSNumber later using setValue and addValue, but you can't change the bit size.

## Parameters

- `valueString`: A C string representing a numeric value for the OSNumber to store.
- `numberOfBits`: The number of bits to limit storage to.

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
- [unsigned64BitValue](osnumber/1808123-unsigned64bitvalue.md)
  Returns the OSNumber object's integer value cast as an unsigned 64-bit integer.
- [unsigned8BitValue](osnumber/1808129-unsigned8bitvalue.md)
  Returns the OSNumber object's integer value cast as an unsigned 8-bit integer.
- [withNumber(unsigned long long, unsigned int)](osnumber/1808143-withnumber.md)
  Creates and initializes an instance of OSNumber with an integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osnumber/1808136-withnumber)*