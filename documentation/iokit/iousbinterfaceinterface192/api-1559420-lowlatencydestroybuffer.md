# LowLatencyDestroyBuffer

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Releases a buffer that was previously allocated using LowLatencyCreateBuffer().

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*LowLatencyDestroyBuffer)(void *self, void *buffer);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNotOpen if the interface is not open for exclusive access. If the buffer was not previously allocated using LowLatencyCreateBuffer() it will return kIOReturnBadArgument.

## Discussion

The interface must be open for the pipe to exist.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `buffer`: Pointer to the buffer previously allocated using LowLatencyCreateBuffer().


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface192/1559420-lowlatencydestroybuffer)*