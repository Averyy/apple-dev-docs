# _maintRequest

**Framework**: Kernel  
**Kind**: instm

Synchronous implementation of addEventSource and removeEventSource functions.

## Declaration

```cpp
virtual IOReturn _maintRequest(
 void *command,
 void *data,
 void *,
 void *);
```

## Return Value

kIOReturnUnsupported if the command given is not implemented, kIOReturnSuccess otherwise.

## Overview

This function implements the commands as defined in the maintCommandEnum. It can be subclassed but it isn't an external API in the usual sense. A subclass implementation of _maintRequest would be called synchronously with respect to the work loop and it should be implemented in the usual way that an ioctl would be.

## See Also

### Miscellaneous
- [addEventSource](./api-1809383-addeventsource.md)
- [disableAllEventSources](./api-1809388-disablealleventsources.md)
  Calls disable() in all event sources.
- [disableAllInterrupts](./api-1809396-disableallinterrupts.md)
  Calls disable() in all interrupt event sources.
- [enableAllEventSources](./api-1809401-enablealleventsources.md)
  Calls enable() in all event sources.
- [enableAllInterrupts](./api-1809404-enableallinterrupts.md)
  Calls enable() in all interrupt event sources.
- [eventSourcePerformsWork](./api-1809410-eventsourceperformswork.md)
  Checks if the event source passed in overrides checkForWork() to perform any work. IOWorkLoop uses this to determine if the event source should be polled in runEventSources() or not.
- [free](./api-1809418-free.md)
- [getThread](./api-1809425-getthread.md)
  Gets the workThread.
- [inGate](./api-1809434-ingate.md)
  Is the current execution context holding the work-loop's gate?
- [init](./api-1809441-init.md)
- [onThread](./api-1809446-onthread.md)
  Is the current execution context on the work thread?
- [removeEventSource](./api-1809449-removeeventsource.md)
- [runAction](./api-1809454-runaction.md)
  Single thread a call to an action with the work-loop.
- [runEventSources](./api-1809459-runeventsources.md)
- [threadMain](./api-1809465-threadmain.md)
- [threadMainContinuation](./api-1809470-threadmaincontinuation.md)
  Static function that calls the threadMain function.
- [workLoop](./api-1809476-workloop.md)
  Factory member function to construct and intialize a work loop.
- [workLoopWithOptions](./api-1809483-workloopwithoptions.md)
  Factory member function to constuct and intialize a work loop.
- [workLoopWithOptions(IOOptionBits options)](./api-1809488-workloopwithoptions.md)
  Factory member function to constuct and intialize a work loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioworkloop/1809377-_maintrequest)*