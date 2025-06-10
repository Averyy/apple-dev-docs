# getFilterAction

**Framework**: Kernel  
**Kind**: instm

Get'ter for filterAction variable.

## Declaration

```swift
virtual Filter getFilterAction() const;
```

#### Return_value

value of filterAction.

## See Also

- [disableInterruptOccurred](iofilterinterrupteventsource/1810540-disableinterruptoccurred.md)
  Override $link IOInterruptEventSource::disableInterruptOccurred to make a filter callout.
- [filterInterruptEventSource](iofilterinterrupteventsource/1810599-filterinterrupteventsource.md)
  Factor method to create and initialise an IOFilterInterruptEventSource. See $link init.
- [init](iofilterinterrupteventsource/1810702-init.md)
  Primary initialiser for the IOFilterInterruptEventSource class.
- [normalInterruptOccurred](iofilterinterrupteventsource/1810739-normalinterruptoccurred.md)
  Override $link IOInterruptEventSource::normalInterruptOccured to make a filter callout.
- [signalInterrupt](iofilterinterrupteventsource/1810772-signalinterrupt.md)
  Cause the work loop to schedule the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource/1810653-getfilteraction)*