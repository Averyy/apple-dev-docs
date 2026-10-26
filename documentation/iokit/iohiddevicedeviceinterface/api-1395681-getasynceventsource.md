# getAsyncEventSource

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Obtains the event source for this IOHIDDeviceDeviceInterface instance.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*getAsyncEventSource)(void *self, CFTypeRef *pSource);
```

#### Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

#### Discussion

The returned event source can be of type CFRunLoopSourceRef or CFRunLoopTimerRef.

## Parameters

- `self`: Pointer to the IOHIDDeviceDeviceInterface.
- `pSource`: Pointer to a CFType to return the run loop event source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicedeviceinterface/1395681-getasynceventsource)*