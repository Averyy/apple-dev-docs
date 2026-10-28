# disable

**Framework**: Kernel  
**Kind**: instm

Disables the notification request.

## Declaration

```cpp
virtual bool disable() = 0;
```

## Return Value

Returns the previous enable state of the IONotifier.

## Overview

Disables the notification request. This method is synchronous with any handler invocations, so when this method returns its guaranteed the handler will not be in entered.

## See Also

### Miscellaneous
- [enable](./api-1810483-enable.md)
  Sets the enable state of the notification request.
- [remove](./api-1810524-remove.md)
  Removes the notification request and releases it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionotifier/1810461-disable)*