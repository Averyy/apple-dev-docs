# GetAddressRange

**Framework**: Kernel  
**Kind**: instm

Returns the address and length of the memory buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
kern_return_t GetAddressRange(IOAddressSegment *range);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes). 

## Parameters

- `range`: An [`IOAddressSegment`](https://developer.apple.com/documentation/driverkit/ioaddresssegment) structure that you provide. On return, this structure contains the address and length of the memory buffer.

## See Also

- [- SetLength](iobuffermemorydescriptor/3180454-setlength.md)
  Changes the length of the memory buffer.
- [IOAddressSegment](../driverkit/ioaddresssegment.md)
  A structure that describes the location and size of a block of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3180453-getaddressrange)*