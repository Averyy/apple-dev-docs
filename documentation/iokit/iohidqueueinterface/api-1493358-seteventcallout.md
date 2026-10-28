# setEventCallout

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the event callout to be called when the queue transitions to non-empty.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*setEventCallout)(void *self, IOHIDCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```

## Return Value

Returns an IOReturn code.

## Discussion

In order for this to work correctly, you must call createAsyncPort and createAsyncEventSource.

## Parameters

- `callback`: if non-NULL is a callback to be called when data is inserted to the queue
- `callbackTarget`: The callback target passed to the callback
- `callbackRefcon`: The callback refcon passed to the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidqueueinterface/1493358-seteventcallout)*