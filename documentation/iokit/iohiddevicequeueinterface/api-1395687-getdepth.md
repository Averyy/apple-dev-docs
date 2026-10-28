# getDepth

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains the queue depth for this IOHIDDeviceQueueInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*getDepth)(void *self, uint32_t *pDepth);
```

## Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Parameters

- `self`: Pointer to the IOHIDDeviceQueueInterface.
- `pDepth`: Pointer to a uint32_t to obtain the number of elements that can be serviced by the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicequeueinterface/1395687-getdepth)*