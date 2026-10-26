# IOFWAVCPCRCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

Callback called after a successful lock transaction to a CMP plug.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
typedef void (*IOFWAVCPCRCallback)(void *refcon, UInt32 generation, UInt16 nodeID, UInt32 plug, UInt32 oldVal, UInt32 newVal);
```

## Parameters

- `refcon`: refcon supplied when a client is registered
- `generation`: Bus generation command was received in
- `nodeID`: is the node originating the request
- `plug`: is the plug number
- `oldVal`: is the value the plug used to contain
- `newVal`: is the quad written into the plug

## See Also

### Callbacks
- [IOFWAVCCommandHandlerCallback](./iofwavccommandhandlercallback.md)
  Callback called when a incoming AVC command matching a registered command handler is received.
- [IOFWAVCRequestCallback](./iofwavcrequestcallback.md)
  This Callback has been deprecated. Use installAVCCommandHandler instead.
- [IOFWAVCSubunitPlugHandlerCallback](./iofwavcsubunitplughandlercallback.md)
  Callback called when a incoming AVC command matching a registered command handler is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofwavcpcrcallback)*