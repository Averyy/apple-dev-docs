# disable

**Framework**: Kernel  
**Kind**: instm

Disables the notification request.

## Declaration

```swift
virtual bool disable() = 0;
```

#### Return_value

Returns the previous enable state of the IONotifier.

#### Overview

Disables the notification request. This method is synchronous with any handler invocations, so when this method returns its guaranteed the handler will not be in entered.

## See Also

- [enable](ionotifier/1810483-enable.md)
  Sets the enable state of the notification request.
- [remove](ionotifier/1810524-remove.md)
  Removes the notification request and releases it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionotifier/1810461-disable)*