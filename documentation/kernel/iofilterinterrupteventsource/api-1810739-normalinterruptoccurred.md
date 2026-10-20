# normalInterruptOccurred

**Framework**: Kernel  
**Kind**: instm

Override $link IOInterruptEventSource::normalInterruptOccured to make a filter callout.

## Declaration

```cpp
virtual void normalInterruptOccurred(
 void *self,
 IOService *prov,
 int ind);
```

## See Also

### Miscellaneous
- [disableInterruptOccurred](./api-1810540-disableinterruptoccurred.md)
  Override $link IOInterruptEventSource::disableInterruptOccurred to make a filter callout.
- [filterInterruptEventSource](./api-1810599-filterinterrupteventsource.md)
  Factor method to create and initialise an IOFilterInterruptEventSource. See $link init.
- [getFilterAction](./api-1810653-getfilteraction.md)
  Get'ter for filterAction variable.
- [init](./api-1810702-init.md)
  Primary initialiser for the IOFilterInterruptEventSource class.
- [signalInterrupt](./api-1810772-signalinterrupt.md)
  Cause the work loop to schedule the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource/1810739-normalinterruptoccurred)*