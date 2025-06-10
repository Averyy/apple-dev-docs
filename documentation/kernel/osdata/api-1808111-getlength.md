# getLength

**Framework**: Kernel  
**Kind**: instm

Returns the number of bytes in or referenced by the OSData object.

## Declaration

```swift
virtual unsigned int getLength() const;
```

#### Return_value

The number of bytes in or referenced by the OSData object.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/1808111-getlength)*