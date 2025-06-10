# filterInterruptEventSource

**Framework**: Kernel  
**Kind**: instm

Factor method to create and initialise an IOFilterInterruptEventSource. See $link init.

## Declaration

```swift
static IOFilterInterruptEventSource * filterInterruptEventSource(
 OSObject *owner, 
 IOInterruptEventSource::Action action, 
 Filter filter, 
 IOService *provider, 
 int intIndex = 0);
```

#### Return_value

a new event source if succesful, 0 otherwise.

## Parameters

- `owner`: Owner/client of this event source.
- `action`: 'C' Function to call when something happens.
- `filter`: 'C' Function to call when interrupt occurs.
- `provider`: Service that provides interrupts.
- `intIndex`: Defaults to 0.

## See Also

- [disableInterruptOccurred](iofilterinterrupteventsource/1810540-disableinterruptoccurred.md)
  Override $link IOInterruptEventSource::disableInterruptOccurred to make a filter callout.
- [getFilterAction](iofilterinterrupteventsource/1810653-getfilteraction.md)
  Get'ter for filterAction variable.
- [init](iofilterinterrupteventsource/1810702-init.md)
  Primary initialiser for the IOFilterInterruptEventSource class.
- [normalInterruptOccurred](iofilterinterrupteventsource/1810739-normalinterruptoccurred.md)
  Override $link IOInterruptEventSource::normalInterruptOccured to make a filter callout.
- [signalInterrupt](iofilterinterrupteventsource/1810772-signalinterrupt.md)
  Cause the work loop to schedule the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource/1810599-filterinterrupteventsource)*