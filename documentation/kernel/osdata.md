# OSData

**Framework**: Kernel  
**Kind**: cl

OSData wraps an array of bytes in a C++ object for use in Libkern collections.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSData : OSObject
```

#### Overview

OSData represents an array of bytes as a Libkern C++ object. OSData objects are mutable: You can add bytes to them and overwrite portions of the byte array.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSData provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
- [appendByte](osdata/1808052-appendbyte.md)
  Appends a single byte value to the OSData object's internal data buffer a specified number of times.
- [appendBytes(const OSData *)](osdata/1808058-appendbytes.md)
  Appends the data contained in another OSData object.
- [appendBytes(const void *, unsigned int)](osdata/1808067-appendbytes.md)
  Appends a buffer of bytes to the OSData object's internal data buffer.
- [ensureCapacity](osdata/1808072-ensurecapacity.md)
  Ensures the array has enough space to store the requested number of bytes.
- [free](osdata/1808080-free.md)
  Deallocates or releases any resources used by the OSDictionary instance.
- [getBytesNoCopy()](osdata/1808085-getbytesnocopy.md)
  Returns a pointer to the OSData object's internal data buffer.
- [getBytesNoCopy(unsigned int, unsigned int)](osdata/1808094-getbytesnocopy.md)
  Returns a pointer into the OSData object's internal data buffer with a given offset and length.
- [getCapacity](osdata/1808100-getcapacity.md)
  Returns the total number of bytes the OSData can store without reallocating.
- [getCapacityIncrement](osdata/1808106-getcapacityincrement.md)
  Returns the storage increment of the OSData object.
- [getLength](osdata/1808111-getlength.md)
  Returns the number of bytes in or referenced by the OSData object.
- [initWithBytes](osdata/1808118-initwithbytes.md)
  Initializes an instance of OSData with a copy of the provided data buffer.
- [initWithBytesNoCopy](osdata/1808127-initwithbytesnocopy.md)
  Initializes an instance of OSData to share the provided data buffer.
- [initWithCapacity](osdata/1808134-initwithcapacity.md)
  Initializes an instance of OSData.
- [initWithData(const OSData *)](osdata/1808141-initwithdata.md)
  Creates and initializes an instance of OSData with contents copied from another OSData object.
- [initWithData(const OSData *, unsigned int, unsigned int)](osdata/1808150-initwithdata.md)
  Initializes an instance of OSData with contents copied from a range within another OSData object.
- [isEqualTo(const OSData *)](osdata/1808160-isequalto.md)
  Tests the equality of two OSData objects.
- [isEqualTo(const OSMetaClassBase *)](osdata/1808165-isequalto.md)
  Tests the equality of an OSData object to an arbitrary object.
- [isEqualTo(const OSString *)](osdata/1808172-isequalto.md)
  Tests the equality of an OSData object to an OSString.
- [isEqualTo(const void *, unsigned int)](osdata/1808178-isequalto.md)
  Tests the equality of an OSData object's contents to a C array of bytes.
- [serialize](osdata/1808185-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](osdata/1808190-setcapacityincrement.md)
  Sets the storage increment of the array.
- [withBytes](osdata/1808195-withbytes.md)
  Creates and initializes an instance of OSData with a copy of the provided data buffer.
- [withBytesNoCopy](osdata/1808197-withbytesnocopy.md)
  Creates and initializes an instance of OSData that shares the provided data buffer.
- [withCapacity](osdata/1808204-withcapacity.md)
  Creates and initializes an empty instance of OSData.
- [withData(const OSData *)](osdata/1808208-withdata.md)
  Creates and initializes an instance of OSData with contents copied from another OSData object.
- [withData(const OSData *, unsigned int, unsigned int)](osdata/1808211-withdata.md)
  Creates and initializes an instance of OSData with contents copied from a range within another OSData object.
### Instance Methods
- [- appendByte](osdata/1387997-appendbyte.md)
- [- appendBytes](osdata/1388036-appendbytes.md)
- [- appendBytes](../driverkit/osdata/appendbytes-38hs5.md)
  Appends a buffer of bytes to the OSData object’s internal data buffer.
- [- ensureCapacity](osdata/1387999-ensurecapacity.md)
- [- free](../driverkit/osdata/free.md)
- [- getBytesNoCopy](../driverkit/osdata/getbytesnocopy-91vcg.md)
  Returns a pointer to the OSData object’s internal data buffer.
- [- getBytesNoCopy](../driverkit/osdata/getbytesnocopy-53puz.md)
  Returns a pointer to the OSData object’s internal data buffer.
- [- getCapacity](../driverkit/osdata/getcapacity.md)
  Returns length of preallocated capacity.
- [- getCapacityIncrement](osdata/1388014-getcapacityincrement.md)
- [- getLength](../driverkit/osdata/getlength.md)
  Returns length of data present.
- [- getMetaClass](osdata/1388028-getmetaclass.md)
- [- initWithBytes](osdata/1388002-initwithbytes.md)
- [- initWithBytesNoCopy](osdata/1388020-initwithbytesnocopy.md)
- [- initWithCapacity](osdata/1388008-initwithcapacity.md)
- [- initWithData](osdata/1388030-initwithdata.md)
- [- initWithData](osdata/3516834-initwithdata.md)
- [- isEqualTo](../driverkit/osdata/isequalto-2kdml.md)
  Compares the data with an OSData
- [- isEqualTo](../driverkit/osdata/isequalto-5ssf5.md)
  Compares the data with an OSString
- [- isEqualTo](../driverkit/osdata/isequalto-79gqy.md)
  Compares the data with a pointer to bytes
- [- isEqualTo](../driverkit/osdata/isequalto-4xz0j.md)
  Compares the data with an OSObject
- [- isSerializable](osdata/2721392-isserializable.md)
- [- serialize](osdata/1388032-serialize.md)
- [- setCapacityIncrement](osdata/1388004-setcapacityincrement.md)
- [- setDeallocFunction](osdata/1388022-setdeallocfunction.md)
- [- setSerializable](osdata/1388038-setserializable.md)
### Type Methods
- [+ withBytes](osdata/1388001-withbytes.md)
- [+ withBytesNoCopy](osdata/1388010-withbytesnocopy.md)
- [+ withCapacity](../driverkit/osdata/withcapacity.md)
  Allocates an OSData object with preallocated capacity.
- [+ withData](../driverkit/osdata/withdata-9y3g.md)
  Allocates an OSData object with a copy of bytes from another OSData.
- [+ withData](../driverkit/osdata/withdata-4rd8n.md)
  Allocates an OSData object with a copy of bytes from a subset of another OSData.

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [OSBoolean](osboolean.md)
  OSBoolean wraps a boolean value in a C++ object for use in Libkern collections.
- [OSString](osstring.md)
  OSString wraps a C string in a C++ object for use in Libkern collections.
- [OSNumber](osnumber.md)
  OSNumber wraps an integer value in a C++ object for use in Libkern collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata)*