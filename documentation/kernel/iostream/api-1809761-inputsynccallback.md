# inputSyncCallback

**Framework**: Kernel  
**Kind**: instm

Input callback function to be implemented by a subclass.

## Declaration

```swift
virtual void inputSyncCallback(
 UInt32token );
```

#### Overview

The inputSyncCallback() method is called as a result of a fast trap from user space. It is called on the same thread as the user request, so no context switch is necessary.

## Parameters

- `token`: A 32-bit token value that can be used by convention to communicate from user space to the stream. The semantics of this value are defined by the IOStream subclass.

## See Also

- [inputCallback](iostream/1809754-inputcallback.md)
  Input callback function to be implemented by a subclass;


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostream/1809761-inputsynccallback)*