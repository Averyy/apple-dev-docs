# runEventSources

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual bool runEventSources();
```

#### Return_value

Return false if the work loop is shutting down, true otherwise.

#### Overview

Consists of the inner 2 loops of the threadMain function(qv). The outer loop terminates when there is no more work, and the inside loop walks the event list calling the checkForWork method in each event source. If an event source has more work to do, it can set the more flag and the outer loop will repeat.

This function can be used to clear a priority inversion between the normal workloop thread and multimedia's real time threads. The problem is that the interrupt action routine is often held off by high priority threads. So if they want to get their data now they will have to call us and ask if any data is available. The multi-media user client will arrange for this function to be called, which causes any pending interrupts to be processed and the completion routines called. By the time the function returns all outstanding work will have been completed at the real time threads priority.

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
- [runAction](ioworkloop/1809454-runaction.md)
  Single thread a call to an action with the work-loop.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioworkloop/1809459-runeventsources)*