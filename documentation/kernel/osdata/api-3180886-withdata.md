# withData

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

Allocates an OSData object with a copy of bytes from another OSData.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```c
static OSDataPtr withData(const OSData *inData);
```

*macOS*

```c
static OSPtr<OSData> withData(const OSData *inData);
```

## Return Value

NULL on failure, otherwise the allocated OSData with reference count 1 to be released by the caller.

## Parameters

- `inData`: An OSData object to copy. The data will be copied at the time of the call.

## See Also

### Creating a Data Object
- [+ withBytes](../../DriverKit/osdata/withbytes.md)
  Allocates an OSData object with a copy of bytes.
- [+ withBytesNoCopy](../../DriverKit/osdata/withbytesnocopy.md)
  Allocates an OSData object with a copy of bytes.
- [+ withCapacity](./api-3180885-withcapacity.md)
  Allocates an OSData object with preallocated capacity.
- [+ withData](./api-3433845-withdata.md)
  Allocates an OSData object with a copy of bytes from a subset of another OSData.
- [OSDataPtr](../../DriverKit/osdataptr.md)
- [- free](./api-3180878-free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdata/3180886-withdata)*