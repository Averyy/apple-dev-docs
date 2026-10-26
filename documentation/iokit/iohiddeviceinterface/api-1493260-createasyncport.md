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

#### Return Value

Returns an IOReturn code.

#### Discussion

The port must be created before any callbacks can be used.

## Parameters

- `port`: Reference to mach port that is created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceinterface/1493260-createasyncport)*