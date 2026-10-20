# getProvider

**Framework**: Kernel  
**Kind**: instm

Get'ter for $link provider variable.

## Declaration

```cpp
virtual const IOService *getProvider() const;
```

#### Return Value

value of provider.

## See Also

### Miscellaneous
- [checkForWork](./api-1812548-checkforwork.md)
  Pure Virtual member function used by IOWorkLoop for issueing a client calls.
- [disable](./api-1812553-disable.md)
  Disable event source.
- [disableInterruptOccurred](./api-1812562-disableinterruptoccurred.md)
  Functions that get called by the interrupt controller.See $link IOService::registerInterrupt
- [enable](./api-1812570-enable.md)
  Enable event source.
- [free](./api-1812582-free.md)
  Sub-class implementation of free method, disconnects from the interrupt source.
- [getAutoDisable](./api-1812592-getautodisable.md)
  Get'ter for $link autoDisable variable.
- [getIntIndex](./api-1812606-getintindex.md)
  Get'ter for $link intIndex interrupt index variable.
- [init](./api-1812641-init.md)
  Primary initialiser for the IOInterruptEventSource class.
- [interruptEventSource](./api-1812661-interrupteventsource.md)
  Factory function for IOInterruptEventSources creation and initialisation.
- [interruptOccurred](./api-1812679-interruptoccurred.md)
  Functions that get called by the interrupt controller. See $link IOService::registerInterrupt
- [normalInterruptOccurred](./api-1812702-normalinterruptoccurred.md)
  Functions that get called by the interrupt controller.See $link IOService::registerInterrupt
- [setWorkLoop](./api-1812729-setworkloop.md)
  Sub-class implementation of setWorkLoop method.
- [warmCPU](./api-1812762-warmcpu.md)
  Tries to reduce latency for an interrupt which will be received near a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerrupteventsource/1812623-getprovider)*