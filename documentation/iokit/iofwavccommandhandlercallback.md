# IOFWAVCCommandHandlerCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

Callback called when a incoming AVC command matching a registered command handler is received.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
typedef IOReturn (*IOFWAVCCommandHandlerCallback)(void *refCon, UInt32 generation, UInt16 srcNodeID, IOFWSpeed speed, const UInt8 *command, UInt32 cmdLen);
```

#### Return Value

The callback handler should return success if it will send the AVC response, or an error if it doesn't want to handle the command

## Parameters

- `refCon`: The refcon supplied when a client is registered
- `generation`: The FireWire bus generation value at the time the command was received
- `srcNodeID`: The node ID of the device who sent us this command
- `speed`: The speed the AVC command packet
- `command`: A pointer to the command bytes
- `cmdLen`: The length of the AVC command bytes buffer in bytes

## See Also

### Callbacks
- [IOFWAVCPCRCallback](./iofwavcpcrcallback.md)
  Callback called after a successful lock transaction to a CMP plug.
- [IOFWAVCRequestCallback](./iofwavcrequestcallback.md)
  This Callback has been deprecated. Use installAVCCommandHandler instead.
- [IOFWAVCSubunitPlugHandlerCallback](./iofwavcsubunitplughandlercallback.md)
  Callback called when a incoming AVC command matching a registered command handler is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofwavccommandhandlercallback)*