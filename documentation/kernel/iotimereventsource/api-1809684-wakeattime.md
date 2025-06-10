# wakeAtTime(AbsoluteTime)

**Framework**: Kernel  
**Kind**: instm

Setup a callback at this absolute time.

## Declaration

```swift
virtual IOReturn wakeAtTime(
 AbsoluteTimeabstime);
```

#### Return_value

kIOReturnSuccess if everything is fine, kIOReturnNoResources if action hasn't been declared by init or IOEventSource::setAction (qqv).

#### Overview

Starts the timer, which will expire at abstime. After it expires, the timer will call the 'action' registered in the init() function. This timer is not periodic, a further call is needed to reset and restart the timer after it expires.

## Parameters

- `abstime`: Absolute Time when to wake up, counted in 'decrementer' units and starts at zero when system boots.

## See Also

- [cancelTimeout](iotimereventsource/1809565-canceltimeout.md)
  Disable any outstanding calls to this event source.
- [disable](iotimereventsource/1809571-disable.md)
  Disable a timed callout.
- [enable](iotimereventsource/1809577-enable.md)
  Enables a call to the action.
- [free](iotimereventsource/1809588-free.md)
  Sub-class implementation of free method, frees calloutEntry
- [init](iotimereventsource/1809597-init.md)
  Initializes the timer with an owner, and a handler to call when the timeout expires.
- [setTimeout(AbsoluteTime)](iotimereventsource/1809607-settimeout.md)
  Setup a callback at after the delay in decrementer ticks. See wakeAtTime(AbsoluteTime).
- [setTimeout(UInt32, UInt32)](iotimereventsource/1809617-settimeout.md)
  Setup a callback at after the delay in some unit. See wakeAtTime(AbsoluteTime).
- [setTimeoutFunc](iotimereventsource/1809624-settimeoutfunc.md)
  Set's timeout as the function of calloutEntry.
- [setTimeoutMS](iotimereventsource/1809629-settimeoutms.md)
  Setup a callback at after the delay in milliseconds. See wakeAtTime(AbsoluteTime).
- [setTimeoutTicks](iotimereventsource/1809639-settimeoutticks.md)
  Setup a callback at after the delay in scheduler ticks. See wakeAtTime(AbsoluteTime).
- [setTimeoutUS](iotimereventsource/1809649-settimeoutus.md)
  Setup a callback at after the delay in microseconds. See wakeAtTime(AbsoluteTime).
- [timeout](iotimereventsource/1809663-timeout.md)
  Function that routes the call from the OS' timeout mechanism into a work-loop context.
- [timerEventSource](iotimereventsource/1809672-timereventsource.md)
  Allocates and returns an initialized timer instance.
- [wakeAtTime(UInt32, UInt32)](iotimereventsource/1809694-wakeattime.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeMS](iotimereventsource/1809708-wakeattimems.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeTicks](iotimereventsource/1809720-wakeattimeticks.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeUS](iotimereventsource/1809737-wakeattimeus.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iotimereventsource/1809684-wakeattime)*