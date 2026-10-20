# SetLength

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Changes the length of the memory buffer.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

*DriverKit*

```cpp
virtual kern_return_t SetLength(uint64_t length);
```

*macOS*

```cpp
kern_return_t SetLength(uint64_t length, OSDispatchMethod supermethod);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md). 

#### Discussion

Use this method to truncate an existing memory buffer. For example, you might call this method when repurposing an existing buffer for a new data type. The maximum capacity of the buffer remains unchanged, but the effective length of the buffer changes to the value you specify. 

## Parameters

- `length`: The new length of the memory buffer. This value must be less than or equal to the buffer's capacity. 

## See Also

### Managing the Buffer Contents
- [- GetAddressRange](./api-3180453-getaddressrange.md)
  Returns the address and length of the memory buffer.
- [IOAddressSegment](../../DriverKit/ioaddresssegment.md)
  A structure that describes the location and size of a block of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3180454-setlength)*