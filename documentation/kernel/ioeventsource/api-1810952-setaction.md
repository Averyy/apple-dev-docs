# setAction

**Framework**: Kernel  
**Kind**: instm

Set'ter for $link action variable.

## Declaration

```swift
virtual void setAction(
 IOEventSource::Actionaction);
```

## Parameters

- `action`: Pointer to a C function of type IOEventSource::Action.

## See Also

- [checkForWork](ioeventsource/1810760-checkforwork.md)
  Virtual member function used by IOWorkLoop for work scheduling.
- [disable](ioeventsource/1810784-disable.md)
  Disable event source.
- [enable](ioeventsource/1810807-enable.md)
  Enable event source.
- [getAction](ioeventsource/1810828-getaction.md)
  Get'ter for $link action variable.
- [getNext](ioeventsource/1810847-getnext.md)
  Get'ter for $link eventChainNext variable.
- [getWorkLoop](ioeventsource/1810872-getworkloop.md)
  Get'ter for $link workLoop variable.
- [init](ioeventsource/1810895-init.md)
  Primary initialiser for the IOEventSource class.
- [isEnabled](ioeventsource/1810913-isenabled.md)
  Get'ter for $link enable variable.
- [onThread](ioeventsource/1810935-onthread.md)
  Convenience function for workLoop->onThread.
- [setNext](ioeventsource/1810967-setnext.md)
  Set'ter for $link eventChainNext variable.
- [setWorkLoop](ioeventsource/1810984-setworkloop.md)
  Set'ter for $link workLoop variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioeventsource/1810952-setaction)*