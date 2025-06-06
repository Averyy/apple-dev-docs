# IOWorkLoop

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOWorkLoop : OSObject
```

#### Overview

An IOWorkLoop is a thread of control that is intended to be used to provide single threaded access to hardware. This class has no knowledge of the nature and type of the events that it marshals and forwards. When a device driver successfully starts (see IOService::start), it is expected to create the event sources it will need to receive events. Then a work loop is initialized and the events are added to the work loop for monitoring. In general this set up will be automated by the family superclass of the specific device.

The thread main method walks the event source linked list and messages each one requesting a work check. At this point each event source is expected to notify its registered owner that the event has occurred. After each event has been walked and each indicates that another loop isn't required (by setting the 'more' flag to false) the thread will go to sleep on a signaling semaphore.

When an event source is registered with a work loop it is informed of the semaphore to use to wake up the loop.

## Topics

### Miscellaneous
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
### Callbacks
- [Action](ioworkloop/action.md)
### DataTypes
- [maintCommandEnum](ioworkloop/maintcommandenum.md)
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [workToDoLock](ioworkloop/worktodolock.md)
- [workToDo](ioworkloop/worktodo.md)
- [workThread](ioworkloop/workthread.md)
- [reserved](ioworkloop/reserved.md)
- [loopRestart](ioworkloop/looprestart.md)
- [gateLock](ioworkloop/gatelock.md)
- [eventChain](ioworkloop/eventchain.md)
- [controlG](ioworkloop/controlg.md)
### Instance Methods
- [- addEventSource](ioworkloop/1567206-addeventsource.md)
- [- closeGate](ioworkloop/1567222-closegate.md)
- [- disableAllEventSources](ioworkloop/1567211-disablealleventsources.md)
- [- disableAllInterrupts](ioworkloop/1567214-disableallinterrupts.md)
- [- enableAllEventSources](ioworkloop/1567209-enablealleventsources.md)
- [- enableAllInterrupts](ioworkloop/1567219-enableallinterrupts.md)
- [- eventSourcePerformsWork](ioworkloop/1567208-eventsourceperformswork.md)
- [- free](ioworkloop/1567200-free.md)
- [- getMetaClass](ioworkloop/1567217-getmetaclass.md)
- [- getThread](ioworkloop/1567218-getthread.md)
- [- inGate](ioworkloop/1567212-ingate.md)
- [- init](ioworkloop/1567216-init.md)
- [- onThread](ioworkloop/1567210-onthread.md)
- [- openGate](ioworkloop/1567207-opengate.md)
- [- removeEventSource](ioworkloop/1567199-removeeventsource.md)
- [- runAction](ioworkloop/1567215-runaction.md)
- [- runActionBlock](ioworkloop/2967279-runactionblock.md)
- [- runEventSources](ioworkloop/1567201-runeventsources.md)
- [- setMaximumLockTime](ioworkloop/1690627-setmaximumlocktime.md)
- [- signalWorkAvailable](ioworkloop/1567205-signalworkavailable.md)
- [- sleepGate](ioworkloop/1567220-sleepgate.md)
- [- sleepGate](ioworkloop/3516505-sleepgate.md)
- [- threadMain](ioworkloop/1567202-threadmain.md)
- [- tryCloseGate](ioworkloop/1567204-tryclosegate.md)
- [- wakeupGate](ioworkloop/1567221-wakeupgate.md)
### Type Methods
- [+ releaseEventChain](ioworkloop/3603592-releaseeventchain.md)
- [+ threadMainContinuation](ioworkloop/1567213-threadmaincontinuation.md)
- [+ workLoop](ioworkloop/1567223-workloop.md)
- [+ workLoopWithOptions](ioworkloop/1567203-workloopwithoptions.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioworkloop)*