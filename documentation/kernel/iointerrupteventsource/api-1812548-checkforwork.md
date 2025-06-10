# checkForWork

**Framework**: Kernel  
**Kind**: instm

Pure Virtual member function used by IOWorkLoop for issueing a client calls.

## Declaration

```swift
virtual bool checkForWork();
```

#### Return_value

Return true if this function needs to be called again before all its outstanding events have been processed.

#### Overview

This function called when the work-loop is ready to check for any work to do and then to call out the owner/action.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerrupteventsource/1812548-checkforwork)*