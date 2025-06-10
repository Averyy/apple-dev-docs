# SetAbortedHandler

**Framework**: Kernel  
**Kind**: instm

Install a handler for the system to call when no other processes reference the action object.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
kern_return_t SetAbortedHandler(OSActionAbortedHandler handler);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See `Error Codes`. 

#### Discussion

The system calls your handler when no other objects reference the action object. If you want to keep the action object, use your handler to retain it. If you don't retain the object, the system releases it shortly after your handler returns.

## Parameters

- `handler`: A handler block for the system to call. Specify   to remove the handler block from your action object.

## See Also

- [+ Create](osaction/3438206-create.md)
  Creates a new action object and configures it with your custom target object and callback method. 
- [- free](osaction/3438209-free.md)
  Performs any final cleanup for the action object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osaction/3438208-setabortedhandler)*