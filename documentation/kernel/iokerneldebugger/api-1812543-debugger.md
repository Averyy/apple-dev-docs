# debugger

**Framework**: Kernel  
**Kind**: instm

Factory method that performs allocation and initialization of an IOKernelDebugger object.

## Declaration

```c
static IOKernelDebugger * debugger(
 IOService *target, 
 IODebuggerTxHandlertxHandler, 
 IODebuggerRxHandlerrxHandler, 
 IODebuggerLinkStatusHandlerlinkStatusHandler, 
 IODebuggerSetModeHandlersetModeHandler);
```

#### Return Value

Returns an IOKernelDebugger instance on success, 0 otherwise.

## Parameters

- `target`: The target object that implements the debugger handlers.
- `txHandler`: The target's transmit handler. A pointer to a 'C' function.
- `rxHandler`: The target's receive handler. A pointer to a 'C' function.
- `linkStatusHandler`: The target's link status handler. A pointer to a 'C' function.
- `setModeHandler`: The target's set mode handler. A pointer to a 'C' function.

## See Also

### Miscellaneous
- [free](./api-1812554-free.md)
  Frees the IOKernelDebugger instance.
- [handleClose](./api-1812560-handleclose.md)
  Handles a client close.
- [handleIsOpen](./api-1812565-handleisopen.md)
  Queries whether a client has an open on this object.
- [handleOpen](./api-1812573-handleopen.md)
  Handles a client open.
- [init](./api-1812584-init.md)
  Initializes an IOKernelDebugger instance.
- [kdpLinkStatusDispatcher](./api-1812595-kdplinkstatusdispatcher.md)
  The KDP link status dispatch function.
- [kdpReceiveDispatcher](./api-1812607-kdpreceivedispatcher.md)
  The KDP receive dispatch function.
- [kdpSetModeDispatcher](./api-1812616-kdpsetmodedispatcher.md)
  The KDP set mode dispatch function.
- [kdpTransmitDispatcher](./api-1812631-kdptransmitdispatcher.md)
  The KDP transmit dispatch function.
- [lock](./api-1812643-lock.md)
  Takes the debugger lock conditionally.
- [nullLinkStatusHandler](./api-1812653-nulllinkstatushandler.md)
  Null link status handler.
- [nullRxHandler](./api-1812663-nullrxhandler.md)
  Null receive handler.
- [nullSetModeHandler](./api-1812671-nullsetmodehandler.md)
  Null set mode handler.
- [nullTxHandler](./api-1812684-nulltxhandler.md)
  Null transmit handler.
- [powerStateDidChangeTo](./api-1812705-powerstatedidchangeto.md)
  Handles notification that the network controller did change power state.
- [powerStateWillChangeTo](./api-1812727-powerstatewillchangeto.md)
  Handles notification that the network controller will change power state.
- [registerHandler](./api-1812741-registerhandler.md)
  Registers the target and the handler functions.
- [signalDebugger](./api-1812763-signaldebugger.md)
  Signal the kernel to enter the debugger when safe.
- [unlock](./api-1812777-unlock.md)
  Releases the debugger lock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iokerneldebugger/1812543-debugger)*