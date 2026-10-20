# enable

**Framework**: Kernel  
**Kind**: instm

overrides in order to set/clear the timed out flag

## Declaration

```cpp
virtual void enable();
```

## See Also

### Miscellaneous
- [ataTimerEventSource](./api-1805559-atatimereventsource.md)
  allocate an instance of this type.
- [cancelTimeout](./api-1805562-canceltimeout.md)
  overrides in order to set/clear the timed out flag
- [disable](./api-1805564-disable.md)
  overrides in order to set/clear the timed out flag
- [hasTimedOut](./api-1805571-hastimedout.md)
  returns true if the timer has expired since the last enable/disable or setTimeout() or wakeAtTime() call.
- [init](./api-1805575-init.md)
- [myTimeout](./api-1805579-mytimeout.md)
  my timeout function which sets the timedOut flag atomically.
- [setTimeoutFunc](./api-1805583-settimeoutfunc.md)
  override to install my timeout function instead of the super's.
- [wakeAtTime](./api-1805589-wakeattime.md)
  overrides in order to set/clear the timed out flag


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/atatimereventsource/1805569-enable)*