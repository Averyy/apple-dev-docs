# interruptEventSource

**Framework**: Kernel  
**Kind**: instm

Factory function for IOInterruptEventSources creation and initialisation.

## Declaration

```swift
static IOInterruptEventSource * interruptEventSource(
 OSObject *owner, 
 Action action, 
 IOService *provider = 0, 
 int intIndex = 0);
```

#### Return_value

A new interrupt event source if successfully created and initialised, 0 otherwise.

## Parameters

- `owner`: Owning client of the new event source.
- `action`: 'C' Function to call when something happens.
- `provider`: IOService that represents the interrupt source. Defaults to 0. When no provider is defined the event source assumes that the client will in some manner call the interruptOccured method explicitly. This will start the ball rolling for safe delivery of asynchronous event's into the driver.
- `intIndex`: The index of the interrupt within the provider's interrupt sources. Defaults to 0, i.e. the first interrupt in the provider.

## See Also

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
- [interruptOccurred](iointerrupteventsource/1812679-interruptoccurred.md)
  Functions that get called by the interrupt controller. See $link IOService::registerInterrupt
- [normalInterruptOccurred](iointerrupteventsource/1812702-normalinterruptoccurred.md)
  Functions that get called by the interrupt controller.See $link IOService::registerInterrupt
- [setWorkLoop](iointerrupteventsource/1812729-setworkloop.md)
  Sub-class implementation of setWorkLoop method.
- [warmCPU](iointerrupteventsource/1812762-warmcpu.md)
  Tries to reduce latency for an interrupt which will be received near a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerrupteventsource/1812661-interrupteventsource)*