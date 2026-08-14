# withData

**Framework**: Kernel  
**Kind**: clm

Allocates an OSData object with a copy of bytes from a subset of another OSData.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
static OSPtr<OSData> withData(const OSData *inData, unsigned int start, unsigned int numBytes);
```

#### Return_value

NULL on failure, otherwise the allocated OSData with reference count 1 to be released by the caller.

## Parameters

- `inData`: An OSData object to copy. The data will be copied at the time of the call.
- `start`: An offset into the OSData object to copy from.
- `numBytes`: The length of data to copy. If (start + numBytes) exceeds the length of inData, the call will fail.

## See Also

- [+ withBytes](../driverkit/osdata/withbytes.md)
  Allocates an OSData object with a copy of bytes.
- [+ withBytesNoCopy](../driverkit/osdata/withbytesnocopy.md)
  Allocates an OSData object with a copy of bytes.
- [+ withCapacity](osdata/3180885-withcapacity.md)
  Allocates an OSData object with preallocated capacity.
- [+ withData](osdata/3180886-withdata.md)
  Allocates an OSData object with a copy of bytes from another OSData.
- [OSDataPtr](../driverkit/osdataptr.md)
- [- free](osdata/3180878-free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3433845-withdata)*