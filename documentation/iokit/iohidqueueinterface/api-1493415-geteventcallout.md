# getEventCallout

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Gets the event callout.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*getEventCallout)(void *self, IOHIDCallbackFunction *outCallback, void **outCallbackTarget, void **outCallbackRefcon);
```

#### Return Value

Returns an IOReturn code.

#### Discussion

This callback will be called the queue transitions to non-empty.

## Parameters

- `outCallback`: if non-NULL is a callback to be called when data is inserted to the queue
- `outCallbackTarget`: The callback target passed to the callback
- `outCallbackRefcon`: The callback refcon passed to the callback


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidqueueinterface/1493415-geteventcallout)*