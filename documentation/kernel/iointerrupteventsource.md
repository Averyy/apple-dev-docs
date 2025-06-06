# IOInterruptEventSource

**Framework**: Kernel  
**Kind**: cl

Event source for interrupt delivery to work-loop based drivers.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOInterruptEventSource : IOEventSource
```

#### Overview

The IOInterruptEventSource is a generic object that delivers calls interrupt routines in it's client in a guaranteed single-threaded manner. IOInterruptEventSource is part of the IOKit $link IOWorkLoop infrastructure where the semantic that one and only one action method is executing within a work-loops event chain.

When the action method is called in the client member function will receive 2 arguments, (IOEventSource *) sender and (int) count, See $link IOInterruptEventSource::Action. Where sender will be reference to the interrupt that occurred and the count will be computed by the difference between the $link producerCount and $link consumerCount. This number may not be reliable as no attempt is made to adjust for around the world type problems but is provided for general information and statistic gathering.

In general a client will use the factory member function to create and initialise the event source and then add it to their work-loop. It is the work loop's responsiblity to maintain the new event source in it's event chain. See $link IOWorkLoop.

An interrupt event source attaches itself to the given provider's interrupt source at initialisation time. At this time it determines if it is connected to a level or edge triggered interrupt. If the interrupt is an level triggered interrupt the event source automatically disables the interrupt source at primary interrupt time and after it call's the client it automatically reenables the interrupt. This action is fairly expensive but it is 100% safe and defaults sensibly so that the driver writer does not have to implement type dependant interrupt routines. So to repeat, the driver writer does not have to be concerned by the actual underlying interrupt mechanism as the event source hides the complexity.

Saying this if the hardware is a multi-device card, for instance a 4 port NIC, where all of the devices are sharing one level triggered interrupt AND it is possible to determine each port's interrupt state non-destructively then the $link IOFilterInterruptEventSource would be a better choice.

Warning: All IOInterruptEventSources are created in the disabled state. If you want to actually schedule interrupt delivery do not forget to enable the source.

## Topics

### Miscellaneous
- [checkForWork](iointerrupteventsource/1812548-checkforwork.md)
  Pure Virtual member function used by IOWorkLoop for issueing a client calls.
- [disable](iointerrupteventsource/1812553-disable.md)
  Disable event source.
- [disableInterruptOccurred](iointerrupteventsource/1812562-disableinterruptoccurred.md)
  Functions that get called by the interrupt controller.See $link IOService::registerInterrupt
- [enable](iointerrupteventsource/1812570-enable.md)
  Enable event source.
- [free](iointerrupteventsource/1812582-free.md)
  Sub-class implementation of free method, disconnects from the interrupt source.
- [getAutoDisable](iointerrupteventsource/1812592-getautodisable.md)
  Get'ter for $link autoDisable variable.
- [getIntIndex](iointerrupteventsource/1812606-getintindex.md)
  Get'ter for $link intIndex interrupt index variable.
- [getProvider](iointerrupteventsource/1812623-getprovider.md)
  Get'ter for $link provider variable.
- [init](iointerrupteventsource/1812641-init.md)
  Primary initialiser for the IOInterruptEventSource class.
- [interruptEventSource](iointerrupteventsource/1812661-interrupteventsource.md)
  Factory function for IOInterruptEventSources creation and initialisation.
- [interruptOccurred](iointerrupteventsource/1812679-interruptoccurred.md)
  Functions that get called by the interrupt controller. See $link IOService::registerInterrupt
- [normalInterruptOccurred](iointerrupteventsource/1812702-normalinterruptoccurred.md)
  Functions that get called by the interrupt controller.See $link IOService::registerInterrupt
- [setWorkLoop](iointerrupteventsource/1812729-setworkloop.md)
  Sub-class implementation of setWorkLoop method.
- [warmCPU](iointerrupteventsource/1812762-warmcpu.md)
  Tries to reduce latency for an interrupt which will be received near a specified time.
### Callbacks
- [Action](ioworkloop/action.md)
### Constants
- [Miscellaneous Defines](iointerrupteventsource/miscellaneous_defines.md)
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iointerrupteventsource/reserved.md)
- [provider](iointerrupteventsource/provider.md)
- [producerCount](iointerrupteventsource/producercount.md)
- [intIndex](iointerrupteventsource/intindex.md)
- [explicitDisable](iointerrupteventsource/explicitdisable.md)
- [consumerCount](iointerrupteventsource/consumercount.md)
- [autoDisable](iointerrupteventsource/autodisable.md)
### Instance Methods
- [- checkForWork](iointerrupteventsource/1577653-checkforwork.md)
- [- disable](iointerrupteventsource/1577654-disable.md)
- [- disableInterruptOccurred](iointerrupteventsource/1577646-disableinterruptoccurred.md)
- [- enable](iointerrupteventsource/1577657-enable.md)
- [- enablePrimaryInterruptTimestamp](iointerrupteventsource/3237243-enableprimaryinterrupttimestamp.md)
- [- free](iointerrupteventsource/1577645-free.md)
- [- getAutoDisable](iointerrupteventsource/1577655-getautodisable.md)
- [- getIntIndex](iointerrupteventsource/1577661-getintindex.md)
- [- getMetaClass](iointerrupteventsource/1577651-getmetaclass.md)
- [- getPrimaryInterruptTimestamp](iointerrupteventsource/3553358-getprimaryinterrupttimestamp.md)
- [- getProvider](iointerrupteventsource/1577650-getprovider.md)
- [- init](iointerrupteventsource/1577649-init.md)
- [- interruptOccurred](iointerrupteventsource/1577659-interruptoccurred.md)
- [- normalInterruptOccurred](iointerrupteventsource/1577662-normalinterruptoccurred.md)
- [- registerInterruptHandler](iointerrupteventsource/1577660-registerinterrupthandler.md)
- [- setWorkLoop](iointerrupteventsource/1577647-setworkloop.md)
- [- unregisterInterruptHandler](iointerrupteventsource/1577644-unregisterinterrupthandler.md)
- [- warmCPU](iointerrupteventsource/1577656-warmcpu.md)
### Type Methods
- [+ interruptEventSource](iointerrupteventsource/1577652-interrupteventsource.md)
- [+ interruptEventSource](iointerrupteventsource/3516456-interrupteventsource.md)

## Relationships

### Inherits From
- [IOEventSource](ioeventsource.md)

## See Also

- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
- [IOInterruptDispatchSourceInterface](iointerruptdispatchsourceinterface.md)
- [IOFilterInterruptEventSource](iofilterinterrupteventsource.md)
  Filtering varient of the $link IOInterruptEventSource.
- [IOInterruptController](iointerruptcontroller.md)
- [PassthruInterruptController](passthruinterruptcontroller.md)
- [IOInterruptSource](iointerruptsource.md)
- [IOInterruptVector](iointerruptvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerrupteventsource)*