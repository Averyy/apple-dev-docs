# runAction

**Framework**: Kernel  
**Kind**: instm

Single thread a call to an action with the work-loop.

## Declaration

```swift
virtual IOReturn runAction(
 Action action,
 OSObject *target, 
 void *arg0 = 0,
 void *arg1 = 0, 
 void *arg2 = 0,
 void *arg3 = 0);
```

#### Return_value

Returns the value of the Action callout.

#### Overview

Client function that causes the given action to be called in a single threaded manner. Beware: the work-loop's gate is recursive and runAction can cause direct or indirect re-entrancy. When executing on a client's thread, runAction will sleep until the work-loop's gate opens for execution of client actions, the action is single threaded against all other work-loop event sources.

## Parameters

- `action`: Pointer to function to be executed in work-loop context.
- `arg0`: Parameter for action parameter, defaults to 0.
- `arg1`: Parameter for action parameter, defaults to 0.
- `arg2`: Parameter for action parameter, defaults to 0.
- `arg3`: Parameter for action parameter, defaults to 0.

## See Also

- [_maintRequest](ioworkloop/1809377-_maintrequest.md)
  Synchronous implementation of addEventSource and removeEventSource functions.
- [addEventSource](ioworkloop/1809383-addeventsource.md)
- [disableAllEventSources](ioworkloop/1809388-disablealleventsources.md)
  Calls disable() in all event sources.
- [disableAllInterrupts](ioworkloop/1809396-disableallinterrupts.md)
  Calls disable() in all interrupt event sources.
- [enableAllEventSources](ioworkloop/1809401-enablealleventsources.md)
  Calls enable() in all event sources.
- [enableAllInterrupts](ioworkloop/1809404-enableallinterrupts.md)
  Calls enable() in all interrupt event sources.
- [eventSourcePerformsWork](ioworkloop/1809410-eventsourceperformswork.md)
  Checks if the event source passed in overrides checkForWork() to perform any work. IOWorkLoop uses this to determine if the event source should be polled in runEventSources() or not.
- [free](ioworkloop/1809418-free.md)
- [getThread](ioworkloop/1809425-getthread.md)
  Gets the workThread.
- [inGate](ioworkloop/1809434-ingate.md)
  Is the current execution context holding the work-loop's gate?
- [init](ioworkloop/1809441-init.md)
- [onThread](ioworkloop/1809446-onthread.md)
  Is the current execution context on the work thread?
- [removeEventSource](ioworkloop/1809449-removeeventsource.md)
- [runEventSources](ioworkloop/1809459-runeventsources.md)
- [threadMain](ioworkloop/1809465-threadmain.md)
- [threadMainContinuation](ioworkloop/1809470-threadmaincontinuation.md)
  Static function that calls the threadMain function.
- [workLoop](ioworkloop/1809476-workloop.md)
  Factory member function to construct and intialize a work loop.
- [workLoopWithOptions](ioworkloop/1809483-workloopwithoptions.md)
  Factory member function to constuct and intialize a work loop.
- [workLoopWithOptions(IOOptionBits options)](ioworkloop/1809488-workloopwithoptions.md)
  Factory member function to constuct and intialize a work loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioworkloop/1809454-runaction)*