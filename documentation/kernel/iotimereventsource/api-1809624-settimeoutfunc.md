# setTimeoutFunc

**Framework**: Kernel  
**Kind**: instm

Set's timeout as the function of calloutEntry.

## Declaration

```cpp
virtual void setTimeoutFunc();
```

## Overview

IOTimerEventSource is based upon the kern/thread_call.h APIs currently. This function allocates the calloutEntry member variable by using thread_call_allocate(timeout, this). If you need to write your own subclass of IOTimerEventSource you probably should override this method to allocate an entry that points to your own timeout routine.

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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iotimereventsource/1809624-settimeoutfunc)*