# createAsyncEventSource

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Creates async eventsource.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*createAsyncEventSource)(void *self, CFRunLoopSourceRef *source);
```

## Return Value

Returns an IOReturn code.

## Discussion

This method will create an async mach port, if one has not already been created.

## Parameters

- `source`: Reference to CFRunLoopSourceRef that is created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface/1493306-createasynceventsource)*