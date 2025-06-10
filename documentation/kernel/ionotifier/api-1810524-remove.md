# remove

**Framework**: Kernel  
**Kind**: instm

Removes the notification request and releases it.

## Declaration

```swift
virtual void remove() = 0;
```

#### Overview

Removes the notification request and release it. Since creating an IONotifier instance will leave it with a retain count of one, creating an IONotifier and then removing it will destroy it. This method is synchronous with any handler invocations, so when this method returns its guaranteed the handler will not be in entered.

## See Also

- [disable](ionotifier/1810461-disable.md)
  Disables the notification request.
- [enable](ionotifier/1810483-enable.md)
  Sets the enable state of the notification request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionotifier/1810524-remove)*