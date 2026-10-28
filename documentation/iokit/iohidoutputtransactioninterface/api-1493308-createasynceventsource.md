# createAsyncEventSource

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Creates an async event source.

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

This will be used with setEventCallout.

## Parameters

- `source`: The newly created event source


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidoutputtransactioninterface/1493308-createasynceventsource)*