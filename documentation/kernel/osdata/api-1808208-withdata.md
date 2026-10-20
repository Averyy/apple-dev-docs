# withData(const OSData *)

**Framework**: Kernel  
**Kind**: instm

Creates and initializes an instance of OSData with contents copied from another OSData object.

## Declaration

```c
static OSData * withData(
 const OSData *inData);
```

#### Return Value

An instance of OSData containing a copy of the data in `inData`, with a reference count of 1; `NULL` on failure.

#### Overview

The new OSData object will grow as needed to accommodate more bytes (*unlike*[CFMutableData](../../CoreFoundation/cfmutabledata.md), for which a nonzero initial capacity is a hard limit).

## Parameters

- `inData`: An OSData object that provides the initial data.

## See Also

### Miscellaneous
- [appendByte](./api-1808052-appendbyte.md)
  Appends a single byte value to the OSData object's internal data buffer a specified number of times.
- [appendBytes(const OSData *)](./api-1808058-appendbytes.md)
  Appends the data contained in another OSData object.
- [appendBytes(const void *, unsigned int)](./api-1808067-appendbytes.md)
  Appends a buffer of bytes to the OSData object's internal data buffer.
- [ensureCapacity](./api-1808072-ensurecapacity.md)
  Ensures the array has enough space to store the requested number of bytes.
- [free](./api-1808080-free.md)
  Deallocates or releases any resources used by the OSDictionary instance.
- [getBytesNoCopy()](./api-1808085-getbytesnocopy.md)
  Returns a pointer to the OSData object's internal data buffer.
- [getBytesNoCopy(unsigned int, unsigned int)](./api-1808094-getbytesnocopy.md)
  Returns a pointer into the OSData object's internal data buffer with a given offset and length.
- [getCapacity](./api-1808100-getcapacity.md)
  Returns the total number of bytes the OSData can store without reallocating.
- [getCapacityIncrement](./api-1808106-getcapacityincrement.md)
  Returns the storage increment of the OSData object.
- [getLength](./api-1808111-getlength.md)
  Returns the number of bytes in or referenced by the OSData object.
- [initWithBytes](./api-1808118-initwithbytes.md)
  Initializes an instance of OSData with a copy of the provided data buffer.
- [initWithBytesNoCopy](./api-1808127-initwithbytesnocopy.md)
  Initializes an instance of OSData to share the provided data buffer.
- [initWithCapacity](./api-1808134-initwithcapacity.md)
  Initializes an instance of OSData.
- [initWithData(const OSData *)](./api-1808141-initwithdata.md)
  Creates and initializes an instance of OSData with contents copied from another OSData object.
- [initWithData(const OSData *, unsigned int, unsigned int)](./api-1808150-initwithdata.md)
  Initializes an instance of OSData with contents copied from a range within another OSData object.
- [isEqualTo(const OSData *)](./api-1808160-isequalto.md)
  Tests the equality of two OSData objects.
- [isEqualTo(const OSMetaClassBase *)](./api-1808165-isequalto.md)
  Tests the equality of an OSData object to an arbitrary object.
- [isEqualTo(const OSString *)](./api-1808172-isequalto.md)
  Tests the equality of an OSData object to an OSString.
- [isEqualTo(const void *, unsigned int)](./api-1808178-isequalto.md)
  Tests the equality of an OSData object's contents to a C array of bytes.
- [serialize](./api-1808185-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setCapacityIncrement](./api-1808190-setcapacityincrement.md)
  Sets the storage increment of the array.
- [withBytes](./api-1808195-withbytes.md)
  Creates and initializes an instance of OSData with a copy of the provided data buffer.
- [withBytesNoCopy](./api-1808197-withbytesnocopy.md)
  Creates and initializes an instance of OSData that shares the provided data buffer.
- [withCapacity](./api-1808204-withcapacity.md)
  Creates and initializes an empty instance of OSData.
- [withData(const OSData *, unsigned int, unsigned int)](./api-1808211-withdata.md)
  Creates and initializes an instance of OSData with contents copied from a range within another OSData object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/1808208-withdata)*