# OSNumber

**Framework**: Kernel  
**Kind**: cl

OSNumber wraps an integer value in a C++ object for use in Libkern collections.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSNumber : OSObject
```

#### Overview

OSNumber represents an integer of 8, 16, 32, or 64 bits as a Libkern C++ object. OSNumber objects are mutable: you can add to or set their values.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSNumber provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
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
- [withNumber(const char *, unsigned int)](osnumber/1808136-withnumber.md)
  Creates and initializes an instance of OSNumber with an unsigned integer value represented as a C string.
- [withNumber(unsigned long long, unsigned int)](osnumber/1808143-withnumber.md)
  Creates and initializes an instance of OSNumber with an integer value.
### Instance Methods
- [- addValue](osnumber/1536683-addvalue.md)
- [- free](../driverkit/osnumber/free.md)
- [- getMetaClass](osnumber/1536671-getmetaclass.md)
- [- init](osnumber/1536668-init.md)
- [- init](osnumber/3516837-init.md)
- [- isEqualTo](../driverkit/osnumber/isequalto-58rb9.md)
  Compares the number with an OSNumber.
- [- isEqualTo](../driverkit/osnumber/isequalto-333kh.md)
  Compares the string with an OSObject
- [- numberOfBits](../driverkit/osnumber/numberofbits.md)
  Returns the number of bits the OSNumber was created with.
- [- numberOfBytes](osnumber/1536680-numberofbytes.md)
- [- serialize](osnumber/1536674-serialize.md)
- [- setValue](osnumber/1536666-setvalue.md)
- [- unsigned16BitValue](../driverkit/osnumber/unsigned16bitvalue.md)
  Returns the value of the OSNumber as a uint16_t value.
- [- unsigned32BitValue](../driverkit/osnumber/unsigned32bitvalue.md)
  Returns the value of the OSNumber as a uint32_t value.
- [- unsigned64BitValue](../driverkit/osnumber/unsigned64bitvalue.md)
  Returns the value of the OSNumber as a uint64_t value.
- [- unsigned8BitValue](../driverkit/osnumber/unsigned8bitvalue.md)
  Returns the value of the OSNumber as a uint8_t value.
### Type Methods
- [+ withNumber](osnumber/1536669-withnumber.md)
- [+ withNumber](osnumber/3516838-withnumber.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [OSBoolean](osboolean.md)
  OSBoolean wraps a boolean value in a C++ object for use in Libkern collections.
- [OSString](osstring.md)
  OSString wraps a C string in a C++ object for use in Libkern collections.
- [OSData](osdata.md)
  OSData wraps an array of bytes in a C++ object for use in Libkern collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osnumber)*