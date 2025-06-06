# ATATimerEventSource

**Framework**: Kernel  
**Kind**: cl

Extend the timer event source to allow checking for timer expiration from behind the workloop.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class ATATimerEventSource : IOTimerEventSource
```

## Topics

### Miscellaneous
- [ataTimerEventSource](atatimereventsource/1805559-atatimereventsource.md)
  allocate an instance of this type.
- [cancelTimeout](atatimereventsource/1805562-canceltimeout.md)
  overrides in order to set/clear the timed out flag
- [disable](atatimereventsource/1805564-disable.md)
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
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](atatimereventsource/reserved.md)
### Instance Methods
- [- cancelTimeout](atatimereventsource/1426556-canceltimeout.md)
- [- disable](atatimereventsource/1426566-disable.md)
- [- enable](atatimereventsource/1426561-enable.md)
- [- getMetaClass](atatimereventsource/1426570-getmetaclass.md)
- [- hasTimedOut](atatimereventsource/1426555-hastimedout.md)
- [- init](atatimereventsource/1426569-init.md)
- [- setTimeoutFunc](atatimereventsource/1426559-settimeoutfunc.md)
- [- wakeAtTime](atatimereventsource/1426557-wakeattime.md)
### Type Methods
- [+ ataTimerEventSource](atatimereventsource/1426553-atatimereventsource.md)
- [+ myTimeout](atatimereventsource/1426564-mytimeout.md)

## Relationships

### Inherits From
- [IOTimerEventSource](iotimereventsource.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/atatimereventsource)*