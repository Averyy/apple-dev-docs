# ConnectQueues

**Framework**: USBSerialDriverKit  
**Kind**: method

Creates and configures the buffers that store the data moving to and from the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t ConnectQueues(IOBufferMemoryDescriptor * * ifmd, IOMemoryDescriptor * * rxqmd, IOMemoryDescriptor * * txqmd, IOMemoryDescriptor * in_rxqmd, IOMemoryDescriptor * in_txqmd, uint32_t in_rxqoffset, uint32_t in_txqoffset, uint8_t in_rxqlogsz, uint8_t in_txqlogsz);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

You do not need to call this method directly. At activation time, an `IOUserUSBSerial` object automatically creates memory buffers for managing data moving to and from the USB device. Calling this method after activation replaces the default queues with the new ones you provide.

If you want to provide the memory buffers yourself, specify those values in the `in_rxqmd` and `in_txqmd` parameters. When creating custom buffers, always make the size of your buffers a power of 2. If you specify `NULL` for `in_rxqmd` and `in_txqmd`, this method creates new buffers for you.

This method returns pointers to the buffers in the `rxqmd` and `txqmd` parameters. It also returns the system-created buffer for storing interrupt-related data in the `ifmd` parameter.

## Parameters

- `ifmd`: On return, a pointer to the memory buffer for storing interrupt-related data.
- `rxqmd`: On return, a pointer to the memory buffer for storing data received from the device.
- `txqmd`: On return, a pointer to the memory buffer for storing data ready to transmit to the device.
- `in_rxqmd`: An existing memory buffer to configure and return in the   parameter. Specify   if you want this method to create the memory buffer for you. If you specify your own buffer object, this method retains it.
- `in_txqmd`: An existing memory buffer to configure and return in the   parameter. Specify   if you want this method to create the memory buffer for you. If you specify your own buffer object, this method retains it.
- `in_rxqoffset`: The offset, in bytes, to the beginning of the   buffer. The offset represents the location at which the system starts accessing the buffer data. Specify   to indicate the beginning of the memory buffer.
- `in_txqoffset`: The offset, in bytes, to the beginning of the   buffer. The offset represents the location at which the system starts accessing the buffer data. Specify   to indicate the beginning of the memory buffer.
- `in_rxqlogsz`: The base-2 logarithmic size of the buffer in the   parameter. For example, specify   for a buffer that is 16 kilobytes (2^14 bytes) in size. If   is  , this method creates a 16 kilobyte buffer regardless of the value in this parameter.
- `in_txqlogsz`: The base-2 logarithmic size of the buffer in the   parameter. For example, specify   for a buffer that is 16 kilobytes (2^14 bytes) in size. If   is  , this method creates a 16 kilobyte buffer regardless of the value in this parameter.

## See Also

- [DisconnectQueues](iouserusbserial/disconnectqueues.md)
  Releases the buffers that manage data moving to and from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial/connectqueues)*