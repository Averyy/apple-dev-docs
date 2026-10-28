# createAsyncPort

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Creates an async port.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
IOReturn (*createAsyncPort)(void *self, mach_port_t *port);
```

## Return Value

Returns an IOReturn code.

## Discussion

This will be used with createAsyncEventSource.

## Parameters

- `port`: The newly created async port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidqueueinterface/1493345-createasyncport)*