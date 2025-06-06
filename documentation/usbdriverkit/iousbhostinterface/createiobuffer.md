# CreateIOBuffer

**Framework**: USBDriverKit  
**Kind**: method

Allocates a buffer for use during I/O operations.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t CreateIOBuffer(IOOptionBits options, uint64_t capacity, IOBufferMemoryDescriptor * * buffer);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method allocates an [`IOBufferMemoryDescriptor`](https://developer.apple.com/documentation/DriverKit/IOBufferMemoryDescriptor) optimized for use by the underlying controller hardware. A buffer allocated by this method isn’t bounced to perform DMA operations.

## Parameters

- `options`: The direction of I/O transfer for the buffer. For a list of possible values, see  .
- `capacity`: The size of the buffer to allocate in bytes.
- `buffer`: A pointer to a variable. On success, this variable contains a pointer to a memory descriptor. It’s your responsibility to release this memory descriptor when you finish using it. If an error occurs, the method returns NULL instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/createiobuffer)*