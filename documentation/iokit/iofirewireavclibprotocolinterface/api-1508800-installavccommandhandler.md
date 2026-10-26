# installAVCCommandHandler

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Installs a command handler for handling specific incoming AVC commands.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*installAVCCommandHandler)(void *self, UInt32 subUnitTypeAndID, UInt32 opCode, void *refCon, IOFWAVCCommandHandlerCallback callback);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `subUnitTypeAndID`: The subunit type and ID for this command handler.
- `opCode`: The opcode for this command handler.
- `refCon`: Arbitrary value passed back as first argument of callback.
- `callback`: A pointer to the callback function


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508800-installavccommandhandler)*