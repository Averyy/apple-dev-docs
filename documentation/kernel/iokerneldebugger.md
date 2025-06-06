# IOKernelDebugger

**Framework**: Kernel  
**Kind**: cl

Kernel debugger nub.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOKernelDebugger : IOService
```

#### Overview

This object interfaces with the KDP (kernel debugger protocol) module and dispatches KDP requests to its target (provider). The target, designated as the debugger device, must implement a pair of handler functions that are called to handle KDP transmit and receive requests during a debugging session. Only a single IOKernelDebugger in the system can be active at a given time. The active IOKernelDebugger is the one that has an IOKDP object attached as a client.

The debugger device is usually a subclass of IOEthernetController. However, any IOService can service an IOKernelDebugger client, implement the two polled mode handlers, and transport the KDP packets through a data channel. However, KDP assumes that the debugger device is an Ethernet interface and therefore it will always send, and expect to receive, an Ethernet frame.

## Topics

### Miscellaneous
- [debugger](iokerneldebugger/1812543-debugger.md)
  Factory method that performs allocation and initialization of an IOKernelDebugger object.
- [free](iokerneldebugger/1812554-free.md)
  Frees the IOKernelDebugger instance.
- [handleClose](iokerneldebugger/1812560-handleclose.md)
  Handles a client close.
- [handleIsOpen](iokerneldebugger/1812565-handleisopen.md)
  Queries whether a client has an open on this object.
- [handleOpen](iokerneldebugger/1812573-handleopen.md)
  Handles a client open.
- [init](iokerneldebugger/1812584-init.md)
  Initializes an IOKernelDebugger instance.
- [kdpLinkStatusDispatcher](iokerneldebugger/1812595-kdplinkstatusdispatcher.md)
  The KDP link status dispatch function.
- [kdpReceiveDispatcher](iokerneldebugger/1812607-kdpreceivedispatcher.md)
  The KDP receive dispatch function.
- [kdpSetModeDispatcher](iokerneldebugger/1812616-kdpsetmodedispatcher.md)
  The KDP set mode dispatch function.
- [kdpTransmitDispatcher](iokerneldebugger/1812631-kdptransmitdispatcher.md)
  The KDP transmit dispatch function.
- [lock](iokerneldebugger/1812643-lock.md)
  Takes the debugger lock conditionally.
- [nullLinkStatusHandler](iokerneldebugger/1812653-nulllinkstatushandler.md)
  Null link status handler.
- [nullRxHandler](iokerneldebugger/1812663-nullrxhandler.md)
  Null receive handler.
- [nullSetModeHandler](iokerneldebugger/1812671-nullsetmodehandler.md)
  Null set mode handler.
- [nullTxHandler](iokerneldebugger/1812684-nulltxhandler.md)
  Null transmit handler.
- [powerStateDidChangeTo](iokerneldebugger/1812705-powerstatedidchangeto.md)
  Handles notification that the network controller did change power state.
- [powerStateWillChangeTo](iokerneldebugger/1812727-powerstatewillchangeto.md)
  Handles notification that the network controller will change power state.
- [registerHandler](iokerneldebugger/1812741-registerhandler.md)
  Registers the target and the handler functions.
- [signalDebugger](iokerneldebugger/1812763-signaldebugger.md)
  Signal the kernel to enter the debugger when safe.
- [unlock](iokerneldebugger/1812777-unlock.md)
  Releases the debugger lock.
### Instance Variables
- [_reserved](iokerneldebugger/reserved.md)
### Instance Methods
- [- free](iokerneldebugger/1434274-free.md)
- [- getMetaClass](iokerneldebugger/1434261-getmetaclass.md)
- [- handleClose](iokerneldebugger/1434255-handleclose.md)
- [- handleIsOpen](iokerneldebugger/1434297-handleisopen.md)
- [- handleOpen](iokerneldebugger/1434247-handleopen.md)
- [- init](iokerneldebugger/1434259-init.md)
- [- message](iokerneldebugger/1434267-message.md)
- [- powerStateDidChangeTo](iokerneldebugger/1434263-powerstatedidchangeto.md)
- [- powerStateWillChangeTo](iokerneldebugger/1434249-powerstatewillchangeto.md)
### Type Methods
- [+ debugger](iokerneldebugger/1434276-debugger.md)
- [+ interfacePublished](iokerneldebugger/1434253-interfacepublished.md)
- [+ kdpLinkStatusDispatcher](iokerneldebugger/1434288-kdplinkstatusdispatcher.md)
- [+ kdpReceiveDispatcher](iokerneldebugger/1434293-kdpreceivedispatcher.md)
- [+ kdpSetModeDispatcher](iokerneldebugger/1434295-kdpsetmodedispatcher.md)
- [+ kdpTransmitDispatcher](iokerneldebugger/1434299-kdptransmitdispatcher.md)
- [+ lock](iokerneldebugger/1434300-lock.md)
- [+ nullLinkStatusHandler](iokerneldebugger/1434245-nulllinkstatushandler.md)
- [+ nullRxHandler](iokerneldebugger/1434243-nullrxhandler.md)
- [+ nullSetModeHandler](iokerneldebugger/1434292-nullsetmodehandler.md)
- [+ nullTxHandler](iokerneldebugger/1434290-nulltxhandler.md)
- [+ registerHandler](iokerneldebugger/1434271-registerhandler.md)
- [+ signalDebugger](iokerneldebugger/1434241-signaldebugger.md)
- [+ unlock](iokerneldebugger/1434281-unlock.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOKitDiagnostics](iokitdiagnostics.md)
- [IOKitDiagnosticsParameters](iokitdiagnosticsparameters.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iokerneldebugger)*