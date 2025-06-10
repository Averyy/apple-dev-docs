# disable

**Framework**: Kernel  
**Kind**: instm

overrides in order to set/clear the timed out flag

## Declaration

```swift
virtual void disable();
```

## See Also

- [ataTimerEventSource](atatimereventsource/1805559-atatimereventsource.md)
  allocate an instance of this type.
- [cancelTimeout](atatimereventsource/1805562-canceltimeout.md)
  overrides in order to set/clear the timed out flag
- [enable](atatimereventsource/1805569-enable.md)
  overrides in order to set/clear the timed out flag
- [hasTimedOut](atatimereventsource/1805571-hastimedout.md)
  returns true if the timer has expired since the last enable/disable or setTimeout() or wakeAtTime() call.
- [init](atatimereventsource/1805575-init.md)
- [myTimeout](atatimereventsource/1805579-mytimeout.md)
  my timeout function which sets the timedOut flag atomically.
- [setTimeoutFunc](atatimereventsource/1805583-settimeoutfunc.md)
  override to install my timeout function instead of the super's.
- [wakeAtTime](atatimereventsource/1805589-wakeattime.md)
  overrides in order to set/clear the timed out flag


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/atatimereventsource/1805564-disable)*