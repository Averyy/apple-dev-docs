# IOFilterInterruptEventSource

**Framework**: Kernel  
**Kind**: cl

Filtering varient of the $link IOInterruptEventSource.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFilterInterruptEventSource : IOInterruptEventSource
```

#### Overview

An interrupt event source that calls the client to determine if a interrupt event needs to be scheduled on the work loop. A filter interrupt event source call's the client in the primary interrupt context, the client can then interrogate its hardware and determine if the interrupt needs to be processed yet.

As the routine is called in the primary interrupt context great care must be taken in the writing of this routine. In general none of the generic IOKit environment is safe to call in this context. We intend this routine to be used by hardware that can interrogate its registers without destroying state. Primarily this variant of event sources will be used by drivers that share interrupts. The filter routine will determine if the interrupt is a real interrupt or a ghost and thus optimise the work thread context switch away.

If you are implementing 'SoftDMA' (or pseudo-DMA), you may not want the I/O Kit to automatically start your interrupt handler routine on your work loop when your filter routine returns true. In this case, you may choose to have your filter routine schedule the work on the work loop itself and then return false. If you do this, the interrupt will not be disabled in hardware and you could receive additional primary interrupts before your work loop–level service routine completes. Because this scheme has implications for synchronization between your filter routine and your interrupt service routine, you should avoid doing this unless your driver requires SoftDMA.

CAUTION: Called in primary interrupt context, if you need to disable interrupt to guard you registers against an unexpected call then it is better to use a straight IOInterruptEventSource and its secondary interrupt delivery mechanism.

## Topics

### Miscellaneous
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
- [signalInterrupt](iofilterinterrupteventsource/1810772-signalinterrupt.md)
  Cause the work loop to schedule the action.
### Callbacks
- [Filter](iofilterinterrupteventsource/filter.md)
### Constants
- [Miscellaneous Defines](iofilterinterrupteventsource/miscellaneous_defines.md)
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iofilterinterrupteventsource/reserved.md)
- [filterAction](iofilterinterrupteventsource/filteraction.md)
### Instance Methods
- [- disableInterruptOccurred](iofilterinterrupteventsource/1515906-disableinterruptoccurred.md)
- [- free](iofilterinterrupteventsource/2967271-free.md)
- [- getFilterAction](iofilterinterrupteventsource/1515908-getfilteraction.md)
- [- getFilterActionBlock](iofilterinterrupteventsource/2967272-getfilteractionblock.md)
- [- getMetaClass](iofilterinterrupteventsource/1515902-getmetaclass.md)
- [- init](iofilterinterrupteventsource/1515901-init.md)
- [- init](iofilterinterrupteventsource/3516455-init.md)
- [- normalInterruptOccurred](iofilterinterrupteventsource/1515904-normalinterruptoccurred.md)
- [- signalInterrupt](iofilterinterrupteventsource/1515903-signalinterrupt.md)
### Type Methods
- [+ filterInterruptEventSource](iofilterinterrupteventsource/1515895-filterinterrupteventsource.md)
- [+ filterInterruptEventSource](iofilterinterrupteventsource/3516454-filterinterrupteventsource.md)
- [+ interruptEventSource](iofilterinterrupteventsource/1515897-interrupteventsource.md)

## Relationships

### Inherits From
- [IOInterruptEventSource](iointerrupteventsource.md)

## See Also

- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
- [IOInterruptDispatchSourceInterface](iointerruptdispatchsourceinterface.md)
- [IOInterruptEventSource](iointerrupteventsource.md)
  Event source for interrupt delivery to work-loop based drivers.
- [IOInterruptController](iointerruptcontroller.md)
- [PassthruInterruptController](passthruinterruptcontroller.md)
- [IOInterruptSource](iointerruptsource.md)
- [IOInterruptVector](iointerruptvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource)*