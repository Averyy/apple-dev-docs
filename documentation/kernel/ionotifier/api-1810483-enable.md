# enable

**Framework**: Kernel  
**Kind**: instm

Sets the enable state of the notification request.

## Declaration

```cpp
virtual void enable(
 boolwas ) = 0;
```

#### Overview

Restores the enable state of the notification request, given the previous state passed in.

## Parameters

- `was`: The enable state of the notifier to restore.

## See Also

### Miscellaneous
- [disable](./api-1810461-disable.md)
  Disables the notification request.
- [remove](./api-1810524-remove.md)
  Removes the notification request and releases it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ionotifier/1810483-enable)*