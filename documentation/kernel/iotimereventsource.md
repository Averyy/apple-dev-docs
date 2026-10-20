# IOTimerEventSource

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

Time based event source mechanism.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOTimerEventSource : IOEventSource
```

#### Overview

An event source that implements a simple timer. A timeout handler is called once the timeout period expires. This timeout handler will be called by the work-loop that this event source is attached to.

Usually a timer event source will be used to implement a timeout. In general when a driver makes a request it will need to setup a call to keep track of when the I/O doesn't complete. This class is designed to make that somewhat easier.

Remember the system doesn't guarantee the accuracy of the callout. It is possible that a higher priority thread is running which will delay the execution of the action routine. In fact the thread will be made runable at the exact requested time, within the accuracy of the CPU's decrementer based interrupt, but the scheduler will then control execution.

## Topics

### Miscellaneous
- [cancelTimeout](./iotimereventsource/api-1809565-canceltimeout.md)
  Disable any outstanding calls to this event source.
- [disable](./iotimereventsource/api-1809571-disable.md)
  Disable a timed callout.
- [enable](./iotimereventsource/api-1809577-enable.md)
  Enables a call to the action.
- [free](./iotimereventsource/api-1809588-free.md)
  Sub-class implementation of free method, frees calloutEntry
- [init](./iotimereventsource/api-1809597-init.md)
  Initializes the timer with an owner, and a handler to call when the timeout expires.
- [setTimeout(AbsoluteTime)](./iotimereventsource/api-1809607-settimeout.md)
  Setup a callback at after the delay in decrementer ticks. See wakeAtTime(AbsoluteTime).
- [setTimeout(UInt32, UInt32)](./iotimereventsource/api-1809617-settimeout.md)
  Setup a callback at after the delay in some unit. See wakeAtTime(AbsoluteTime).
- [setTimeoutFunc](./iotimereventsource/api-1809624-settimeoutfunc.md)
  Set's timeout as the function of calloutEntry.
- [setTimeoutMS](./iotimereventsource/api-1809629-settimeoutms.md)
  Setup a callback at after the delay in milliseconds. See wakeAtTime(AbsoluteTime).
- [setTimeoutTicks](./iotimereventsource/api-1809639-settimeoutticks.md)
  Setup a callback at after the delay in scheduler ticks. See wakeAtTime(AbsoluteTime).
- [setTimeoutUS](./iotimereventsource/api-1809649-settimeoutus.md)
  Setup a callback at after the delay in microseconds. See wakeAtTime(AbsoluteTime).
- [timeout](./iotimereventsource/api-1809663-timeout.md)
  Function that routes the call from the OS' timeout mechanism into a work-loop context.
- [timerEventSource](./iotimereventsource/api-1809672-timereventsource.md)
  Allocates and returns an initialized timer instance.
- [wakeAtTime(AbsoluteTime)](./iotimereventsource/api-1809684-wakeattime.md)
  Setup a callback at this absolute time.
- [wakeAtTime(UInt32, UInt32)](./iotimereventsource/api-1809694-wakeattime.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeMS](./iotimereventsource/api-1809708-wakeattimems.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeTicks](./iotimereventsource/api-1809720-wakeattimeticks.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeUS](./iotimereventsource/api-1809737-wakeattimeus.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
### Callbacks
- [Action](./ioworkloop/action.md)
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./iotimereventsource/reserved.md)
- [calloutEntry](./iotimereventsource/calloutentry.md)
- [abstime](./iotimereventsource/abstime.md)
### Instance Methods
- [- cancelTimeout](./iotimereventsource/api-1576144-canceltimeout.md)
- [- checkForWork](./iotimereventsource/api-2870317-checkforwork.md)
- [- disable](./iotimereventsource/api-1576150-disable.md)
- [- enable](./iotimereventsource/api-1576151-enable.md)
- [- free](./iotimereventsource/api-1576139-free.md)
- [- getMetaClass](./iotimereventsource/api-1576143-getmetaclass.md)
- [- init](./iotimereventsource/api-1576153-init.md)
- [- init](./iotimereventsource/api-3516494-init.md)
- [- setTimeout](./iotimereventsource/api-1576149-settimeout.md)
- [- setTimeout](./iotimereventsource/api-3516495-settimeout.md)
- [- setTimeout](./iotimereventsource/api-3516496-settimeout.md)
- [- setTimeoutFunc](./iotimereventsource/api-1576136-settimeoutfunc.md)
- [- setTimeoutMS](./iotimereventsource/api-1576137-settimeoutms.md)
- [- setTimeoutTicks](./iotimereventsource/api-1576140-settimeoutticks.md)
- [- setTimeoutUS](./iotimereventsource/api-1576152-settimeoutus.md)
- [- setWorkLoop](./iotimereventsource/api-1576138-setworkloop.md)
- [- wakeAtTime](./iotimereventsource/api-1576147-wakeattime.md)
- [- wakeAtTime](./iotimereventsource/api-3516499-wakeattime.md)
- [- wakeAtTime](./iotimereventsource/api-3516500-wakeattime.md)
- [- wakeAtTimeMS](./iotimereventsource/api-1576141-wakeattimems.md)
- [- wakeAtTimeTicks](./iotimereventsource/api-1576154-wakeattimeticks.md)
- [- wakeAtTimeUS](./iotimereventsource/api-1576145-wakeattimeus.md)
### Type Methods
- [+ timeout](./iotimereventsource/api-1576142-timeout.md)
- [+ timeoutAndRelease](./iotimereventsource/api-1576146-timeoutandrelease.md)
- [+ timeoutSignaled](./iotimereventsource/api-2870321-timeoutsignaled.md)
- [+ timerEventSource](./iotimereventsource/api-1576148-timereventsource.md)
- [+ timerEventSource](./iotimereventsource/api-3516497-timereventsource.md)
- [+ timerEventSource](./iotimereventsource/api-3516498-timereventsource.md)

## Relationships

### Inherits From
- [IOEventSource](./ioeventsource.md)

## See Also

### Timers
- [IOWatchDogTimer](./iowatchdogtimer.md)
- [IOGetTime](./api-1575332-iogettime.md)
- [IOTimeStampConstant](./api-1535203-iotimestampconstant.md)
- [IOTimeStampEndConstant](./api-1535232-iotimestampendconstant.md)
- [IOTimeStampStartConstant](./api-1535234-iotimestampstartconstant.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iotimereventsource)*