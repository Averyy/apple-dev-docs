# enable

**Framework**: Kernel  
**Kind**: instm

Enables a call to the action.

## Declaration

```cpp
virtual void enable();
```

## Overview

Allows the action function to be called. If the timer event source was disabled while a call was outstanding and the call wasn't cancelled then it will be rescheduled. So a disable/enable pair will disable calls from this event source.

## See Also

### Miscellaneous
- [cancelTimeout](./api-1809565-canceltimeout.md)
  Disable any outstanding calls to this event source.
- [disable](./api-1809571-disable.md)
  Disable a timed callout.
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
- [wakeAtTime(AbsoluteTime)](./api-1809684-wakeattime.md)
  Setup a callback at this absolute time.
- [wakeAtTime(UInt32, UInt32)](./api-1809694-wakeattime.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeMS](./api-1809708-wakeattimems.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeTicks](./api-1809720-wakeattimeticks.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).
- [wakeAtTimeUS](./api-1809737-wakeattimeus.md)
  Setup a callback at this absolute time. See wakeAtTime(AbsoluteTime).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iotimereventsource/1809577-enable)*