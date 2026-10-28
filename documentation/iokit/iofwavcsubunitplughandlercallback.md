# IOFWAVCSubunitPlugHandlerCallback

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

Callback called when a incoming AVC command matching a registered command handler is received.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
typedef IOReturn (*IOFWAVCSubunitPlugHandlerCallback)(void *refCon, UInt32 subunitTypeAndID, IOFWAVCPlugTypes plugType, UInt32 plugNum, IOFWAVCSubunitPlugMessages plugMessage, UInt32 messageParams);
```

## Return Value

The return value is only pertinent for the kIOFWAVCSubunitPlugMsgSignalFormatModified message. Return an error if not accepting the sig format change.

## Parameters

- `refCon`: The refcon supplied when a client is registered
- `subunitTypeAndID`: The subunit type and id of this plug
- `plugType`: The type of plug receiving the message
- `plugNum`: The number of the plug receiving the message
- `plugMessage`: The plug message
- `messageParams`: The parameters associated with the plug message

## See Also

### Callbacks
- [IOFWAVCCommandHandlerCallback](./iofwavccommandhandlercallback.md)
  Callback called when a incoming AVC command matching a registered command handler is received.
- [IOFWAVCPCRCallback](./iofwavcpcrcallback.md)
  Callback called after a successful lock transaction to a CMP plug.
- [IOFWAVCRequestCallback](./iofwavcrequestcallback.md)
  This Callback has been deprecated. Use installAVCCommandHandler instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofwavcsubunitplughandlercallback)*