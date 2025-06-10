# signalInterrupt

**Framework**: Kernel  
**Kind**: instm

Cause the work loop to schedule the action.

## Declaration

```swift
virtual void signalInterrupt();
```

#### Overview

Cause the work loop to schedule the interrupt action even if the filter routine returns 'false'. Note well the interrupting condition MUST be cleared from the hardware otherwise an infinite process interrupt loop will occur. Use this function when SoftDMA is desired. See $link IOFilterInterruptSource::Filter

## See Also

- [disableInterruptOccurred](iofilterinterrupteventsource/1810540-disableinterruptoccurred.md)
  Override $link IOInterruptEventSource::disableInterruptOccurred to make a filter callout.
- [filterInterruptEventSource](iofilterinterrupteventsource/1810599-filterinterrupteventsource.md)
  Factor method to create and initialise an IOFilterInterruptEventSource. See $link init.
- [getFilterAction](iofilterinterrupteventsource/1810653-getfilteraction.md)
  Get'ter for filterAction variable.
- [init](iofilterinterrupteventsource/1810702-init.md)
  Primary initialiser for the IOFilterInterruptEventSource class.
- [normalInterruptOccurred](iofilterinterrupteventsource/1810739-normalinterruptoccurred.md)
  Override $link IOInterruptEventSource::normalInterruptOccured to make a filter callout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource/1810772-signalinterrupt)*