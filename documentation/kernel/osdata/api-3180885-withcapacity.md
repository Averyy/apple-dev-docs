# withCapacity

**Framework**: Kernel  
**Kind**: clm

Allocates an OSData object with preallocated capacity.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
static OSPtr<OSData> withCapacity(unsigned int capacity);
```

#### Return_value

NULL on failure, otherwise the allocated OSData with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSData object with preallocated capacity. The OSData will have zero length until data is added to it with appendBytes().

## Parameters

- `capacity`: Number of bytes of data the object can hold.

## See Also

- [+ withBytes](../driverkit/osdata/withbytes.md)
  Allocates an OSData object with a copy of bytes.
- [+ withBytesNoCopy](../driverkit/osdata/withbytesnocopy.md)
  Allocates an OSData object with a copy of bytes.
- [+ withData](osdata/3180886-withdata.md)
  Allocates an OSData object with a copy of bytes from another OSData.
- [+ withData](osdata/3433845-withdata.md)
  Allocates an OSData object with a copy of bytes from a subset of another OSData.
- [OSDataPtr](../driverkit/osdataptr.md)
- [- free](osdata/3180878-free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3180885-withcapacity)*