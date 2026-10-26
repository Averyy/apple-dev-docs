# setValueAvailableCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets callback to be used when the queue transitions to non-empty.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*setValueAvailableCallback)(void *self, IOHIDCallback callback, void *context);
```

#### Return Value

Returns kIOReturnSuccess if successful or a kern_return_t if unsuccessful.

#### Discussion

In order to make use of asynchronous behavior, the event source obtained using getAsyncEventSource must be added to a run loop.

## Parameters

- `self`: Pointer to the IOHIDDeviceQueueInterface.
- `callback`: Callback of type IOHIDCallback to be used when data is placed on the queue.
- `context`: Pointer to data to be passed to the callback.
- `options`: Reserved for future use. Ignored in current implementation. Set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicequeueinterface/1395721-setvalueavailablecallback)*