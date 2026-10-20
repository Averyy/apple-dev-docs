# IOKernelDebugger

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

Kernel debugger nub.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOKernelDebugger : IOService
```

#### Overview

This object interfaces with the KDP (kernel debugger protocol) module and dispatches KDP requests to its target (provider). The target, designated as the debugger device, must implement a pair of handler functions that are called to handle KDP transmit and receive requests during a debugging session. Only a single IOKernelDebugger in the system can be active at a given time. The active IOKernelDebugger is the one that has an IOKDP object attached as a client.

The debugger device is usually a subclass of IOEthernetController. However, any IOService can service an IOKernelDebugger client, implement the two polled mode handlers, and transport the KDP packets through a data channel. However, KDP assumes that the debugger device is an Ethernet interface and therefore it will always send, and expect to receive, an Ethernet frame.

## Topics

### Miscellaneous
- [debugger](./iokerneldebugger/api-1812543-debugger.md)
  Factory method that performs allocation and initialization of an IOKernelDebugger object.
- [free](./iokerneldebugger/api-1812554-free.md)
  Frees the IOKernelDebugger instance.
- [handleClose](./iokerneldebugger/api-1812560-handleclose.md)
  Handles a client close.
- [handleIsOpen](./iokerneldebugger/api-1812565-handleisopen.md)
  Queries whether a client has an open on this object.
- [handleOpen](./iokerneldebugger/api-1812573-handleopen.md)
  Handles a client open.
- [init](./iokerneldebugger/api-1812584-init.md)
  Initializes an IOKernelDebugger instance.
- [kdpLinkStatusDispatcher](./iokerneldebugger/api-1812595-kdplinkstatusdispatcher.md)
  The KDP link status dispatch function.
- [kdpReceiveDispatcher](./iokerneldebugger/api-1812607-kdpreceivedispatcher.md)
  The KDP receive dispatch function.
- [kdpSetModeDispatcher](./iokerneldebugger/api-1812616-kdpsetmodedispatcher.md)
  The KDP set mode dispatch function.
- [kdpTransmitDispatcher](./iokerneldebugger/api-1812631-kdptransmitdispatcher.md)
  The KDP transmit dispatch function.
- [lock](./iokerneldebugger/api-1812643-lock.md)
  Takes the debugger lock conditionally.
- [nullLinkStatusHandler](./iokerneldebugger/api-1812653-nulllinkstatushandler.md)
  Null link status handler.
- [nullRxHandler](./iokerneldebugger/api-1812663-nullrxhandler.md)
  Null receive handler.
- [nullSetModeHandler](./iokerneldebugger/api-1812671-nullsetmodehandler.md)
  Null set mode handler.
- [nullTxHandler](./iokerneldebugger/api-1812684-nulltxhandler.md)
  Null transmit handler.
- [powerStateDidChangeTo](./iokerneldebugger/api-1812705-powerstatedidchangeto.md)
  Handles notification that the network controller did change power state.
- [powerStateWillChangeTo](./iokerneldebugger/api-1812727-powerstatewillchangeto.md)
  Handles notification that the network controller will change power state.
- [registerHandler](./iokerneldebugger/api-1812741-registerhandler.md)
  Registers the target and the handler functions.
- [signalDebugger](./iokerneldebugger/api-1812763-signaldebugger.md)
  Signal the kernel to enter the debugger when safe.
- [unlock](./iokerneldebugger/api-1812777-unlock.md)
  Releases the debugger lock.
### Instance Variables
- [_reserved](./iokerneldebugger/reserved.md)
### Instance Methods
- [- free](./iokerneldebugger/api-1434274-free.md)
- [- getMetaClass](./iokerneldebugger/api-1434261-getmetaclass.md)
- [- handleClose](./iokerneldebugger/api-1434255-handleclose.md)
- [- handleIsOpen](./iokerneldebugger/api-1434297-handleisopen.md)
- [- handleOpen](./iokerneldebugger/api-1434247-handleopen.md)
- [- init](./iokerneldebugger/api-1434259-init.md)
- [- message](./iokerneldebugger/api-1434267-message.md)
- [- powerStateDidChangeTo](./iokerneldebugger/api-1434263-powerstatedidchangeto.md)
- [- powerStateWillChangeTo](./iokerneldebugger/api-1434249-powerstatewillchangeto.md)
### Type Methods
- [+ debugger](./iokerneldebugger/api-1434276-debugger.md)
- [+ interfacePublished](./iokerneldebugger/api-1434253-interfacepublished.md)
- [+ kdpLinkStatusDispatcher](./iokerneldebugger/api-1434288-kdplinkstatusdispatcher.md)
- [+ kdpReceiveDispatcher](./iokerneldebugger/api-1434293-kdpreceivedispatcher.md)
- [+ kdpSetModeDispatcher](./iokerneldebugger/api-1434295-kdpsetmodedispatcher.md)
- [+ kdpTransmitDispatcher](./iokerneldebugger/api-1434299-kdptransmitdispatcher.md)
- [+ lock](./iokerneldebugger/api-1434300-lock.md)
- [+ nullLinkStatusHandler](./iokerneldebugger/api-1434245-nulllinkstatushandler.md)
- [+ nullRxHandler](./iokerneldebugger/api-1434243-nullrxhandler.md)
- [+ nullSetModeHandler](./iokerneldebugger/api-1434292-nullsetmodehandler.md)
- [+ nullTxHandler](./iokerneldebugger/api-1434290-nulltxhandler.md)
- [+ registerHandler](./iokerneldebugger/api-1434271-registerhandler.md)
- [+ signalDebugger](./iokerneldebugger/api-1434241-signaldebugger.md)
- [+ unlock](./iokerneldebugger/api-1434281-unlock.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Debugging
- [IOKitDiagnostics](./iokitdiagnostics.md)
- [IOKitDiagnosticsParameters](./iokitdiagnosticsparameters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iokerneldebugger)*