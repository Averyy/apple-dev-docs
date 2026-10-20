# setWorkLoop

**Framework**: Kernel  
**Kind**: instm

Set'ter for $link workLoop variable.

## Declaration

```cpp
virtual void setWorkLoop(
 IOWorkLoop *workLoop);
```

## Parameters

- `workLoop`: Target work-loop of this event source instance. A subclass of IOWorkLoop that at least reacts to signalWorkAvailable() and onThread functions.

## See Also

### Miscellaneous
- [checkForWork](./api-1810760-checkforwork.md)
  Virtual member function used by IOWorkLoop for work scheduling.
- [disable](./api-1810784-disable.md)
  Disable event source.
- [enable](./api-1810807-enable.md)
  Enable event source.
- [getAction](./api-1810828-getaction.md)
  Get'ter for $link action variable.
- [getNext](./api-1810847-getnext.md)
  Get'ter for $link eventChainNext variable.
- [getWorkLoop](./api-1810872-getworkloop.md)
  Get'ter for $link workLoop variable.
- [init](./api-1810895-init.md)
  Primary initialiser for the IOEventSource class.
- [isEnabled](./api-1810913-isenabled.md)
  Get'ter for $link enable variable.
- [onThread](./api-1810935-onthread.md)
  Convenience function for workLoop->onThread.
- [setAction](./api-1810952-setaction.md)
  Set'ter for $link action variable.
- [setNext](./api-1810967-setnext.md)
  Set'ter for $link eventChainNext variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioeventsource/1810984-setworkloop)*