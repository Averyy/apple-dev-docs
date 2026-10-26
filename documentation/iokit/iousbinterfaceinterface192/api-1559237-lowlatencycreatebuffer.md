# LowLatencyCreateBuffer

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Allocates a buffer of type bufferType.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*LowLatencyCreateBuffer)(void *self, void **buffer, IOByteCount size, UInt32 bufferType);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNotOpen if the interface is not open for exclusive access. If the buffer can't be allocated, it will return kIOReturnNoMemory.

#### Discussion

This function allocates a buffer of type bufferType. The buffer can then be used with the LowLatencyIsochReadPipeAsync() or LowLatencyIsochWritePipeAsync() calls.

The LowLatencyIsochReadPipeAsync() or LowLatencyIsochWritePipeAsync() calls require the clients to pre-allocate the data buffer and the frame list buffer parameters. This call is used to allocate those buffers. After the client is done using the buffers, they need to be released through the LowLatencyDestroyBuffer() call.

If the buffer is to be used for reading data, the type passed in should be kUSBLowLatencyReadBuffer. If the buffer is to be used for writing data, the type should be kUSBLowLatencyWriteBuffer. For frame list data, the type should be kUSBLowLatencyFrameListBuffer.

The client can create multiple data and frame list buffers, or it can allocate a large buffer and then use only a portion of the buffer in calls to LowLatencyReadIsochPipeAsync() or LowLatencyWriteIsochPipeAsync().

The interface must be open for the pipe to exist.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `buffer`: Pointer to a pointer that will receive the pointer to the buffer created by this call.
- `size`: The size of the buffer to be created in bytes.
- `bufferType`: Type of buffer: one of kUSBLowLatencyWriteBuffer, kUSBLowLatencyReadBuffer, or kUSBLowLatencyFrameListBuffer. See the documentation for USB.h.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface192/1559237-lowlatencycreatebuffer)*