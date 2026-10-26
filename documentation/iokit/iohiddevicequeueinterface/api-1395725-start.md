# start

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Starts element value delivery to the queue.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*start)(void *self, IOOptionBits options);
```

#### Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

## Parameters

- `self`: Pointer to the IOHIDDeviceQueueInterface.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicequeueinterface/1395725-start)*