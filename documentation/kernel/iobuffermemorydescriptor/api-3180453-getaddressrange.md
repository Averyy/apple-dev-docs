# GetAddressRange

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns the address and length of the memory buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```c
kern_return_t GetAddressRange(IOAddressSegment *range);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md). 

## Parameters

- `range`: An [`IOAddressSegment`](../../DriverKit/ioaddresssegment.md) structure that you provide. On return, this structure contains the address and length of the memory buffer.

## See Also

### Managing the Buffer Contents
- [- SetLength](./api-3180454-setlength.md)
  Changes the length of the memory buffer.
- [IOAddressSegment](../../DriverKit/ioaddresssegment.md)
  A structure that describes the location and size of a block of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3180453-getaddressrange)*