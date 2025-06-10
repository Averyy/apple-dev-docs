# checkForWork

**Framework**: Kernel  
**Kind**: instm

Virtual member function used by IOWorkLoop for work scheduling.

## Declaration

```swift
virtual bool checkForWork();
```

#### Return_value

Return true if this function needs to be called again before all its outstanding events have been processed.

#### Overview

This function will be called to request a subclass to check its internal state for any work to do and then to call out the owner/action. If this event source never performs any work (e.g. IOCommandGate), this method should not be overridden. NOTE: This method is no longer declared pure virtual. A default implementation is provided in IOEventSource.

## See Also

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
- [setAction](ioeventsource/1810952-setaction.md)
  Set'ter for $link action variable.
- [setNext](ioeventsource/1810967-setnext.md)
  Set'ter for $link eventChainNext variable.
- [setWorkLoop](ioeventsource/1810984-setworkloop.md)
  Set'ter for $link workLoop variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioeventsource/1810760-checkforwork)*