# disable

**Framework**: Kernel  
**Kind**: instm

Disable event source.

## Declaration

```cpp
virtual void disable();
```

## Overview

A subclass implementation is expected to respect the enabled state when checkForWork is called.

## See Also

### Miscellaneous
- [checkForWork](./api-1810760-checkforwork.md)
  Virtual member function used by IOWorkLoop for work scheduling.
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
- [setWorkLoop](./api-1810984-setworkloop.md)
  Set'ter for $link workLoop variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioeventsource/1810784-disable)*