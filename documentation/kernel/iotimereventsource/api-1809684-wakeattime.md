# wakeAtTime(AbsoluteTime)

**Framework**: Kernel  
**Kind**: instm

Setup a callback at this absolute time.

## Declaration

```cpp
virtual IOReturn wakeAtTime(
 AbsoluteTimeabstime);
```

#### Return Value

kIOReturnSuccess if everything is fine, kIOReturnNoResources if action hasn't been declared by init or IOEventSource::setAction (qqv).

#### Overview

Starts the timer, which will expire at abstime. After it expires, the timer will call the 'action' registered in the init() function. This timer is not periodic, a further call is needed to reset and restart the timer after it expires.

## Parameters

- `abstime`: Absolute Time when to wake up, counted in 'decrementer' units and starts at zero when system boots.

## See Also

### Miscellaneous
- [cancelTimeout](./api-1809565-canceltimeout.md)
  Disable any outstanding calls to this event source.
- [disable](./api-1809571-disable.md)
  Disable a timed callout.
- [enable](./api-1809577-enable.md)
  Enables a call to the action.
- [free](./api-1809588-free.md)
  Sub-class implementation of free method, frees calloutEntry
- [init](./api-1809597-init.md)
  Initializes the timer with an owner, and a handler to call when the timeout expires.
- [setTimeout(AbsoluteTime)](./api-1809607-settimeout.md)
  Setup a callback at after the delay in decrementer ticks. See wakeAtTime(AbsoluteTime).
- [setTimeout(UInt32, UInt32)](./api-1809617-settimeout.md)
  Setup a callback at after the delay in some unit. See wakeAtTime(AbsoluteTime).
- [setTimeoutFunc](./api-1809624-settimeoutfunc.md)
  Set's timeout as the function of calloutEntry.
- [setTimeoutMS](./api-1809629-settimeoutms.md)
  Setup a callback at after the delay in milliseconds. See wakeAtTime(AbsoluteTime).
- [setTimeoutTicks](./api-1809639-settimeoutticks.md)
  Setup a callback at after the delay in scheduler ticks. See wakeAtTime(AbsoluteTime).
- [setTimeoutUS](./api-1809649-settimeoutus.md)
  Setup a callback at after the delay in microseconds. See wakeAtTime(AbsoluteTime).
- [timeout](./api-1809663-timeout.md)
  Function that routes the call from the OS' timeout mechanism into a work-loop context.
- [timerEventSource](./api-1809672-timereventsource.md)
  Allocates and returns an initialized timer instance.
- [wakeAtTime(UInt32, UInt32)](./api-1809694-wakeattime.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeMS](./api-1809708-wakeattimems.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeTicks](./api-1809720-wakeattimeticks.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeUS](./api-1809737-wakeattimeus.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iotimereventsource/1809684-wakeattime)*