# unlock

**Framework**: Kernel  
**Kind**: instm

Releases the debugger lock.

## Declaration

```swift
static void unlock(
 IODebuggerLockState state );
```

#### Overview

This method releases the debugger lock if the kIODebuggerLockTaken flag is set in the argument.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iokerneldebugger/1812777-unlock)*