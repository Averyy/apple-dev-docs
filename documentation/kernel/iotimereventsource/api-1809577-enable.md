# enable

**Framework**: Kernel  
**Kind**: instm

Enables a call to the action.

## Declaration

```swift
virtual void enable();
```

#### Overview

Allows the action function to be called. If the timer event source was disabled while a call was outstanding and the call wasn't cancelled then it will be rescheduled. So a disable/enable pair will disable calls from this event source.

## See Also

- [cancelTimeout](iotimereventsource/1809565-canceltimeout.md)
  Disable any outstanding calls to this event source.
- [disable](iotimereventsource/1809571-disable.md)
  Disable a timed callout.
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
- [wakeAtTime(AbsoluteTime)](iotimereventsource/1809684-wakeattime.md)
  Setup a callback at this absolute time.
- [wakeAtTime(UInt32, UInt32)](iotimereventsource/1809694-wakeattime.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeMS](iotimereventsource/1809708-wakeattimems.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeTicks](iotimereventsource/1809720-wakeattimeticks.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeUS](iotimereventsource/1809737-wakeattimeus.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iotimereventsource/1809577-enable)*