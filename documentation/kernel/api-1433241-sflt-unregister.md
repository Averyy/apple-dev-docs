# sflt_unregister

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

## Declaration

```swift
errno_t sflt_unregister(sflt_handle handle);
```

#### Return_value

0 on success otherwise the errno error.

#### Discussion

Unregisters a socket filter. This will not detach the socket filter from all sockets it may be attached to at the time, it will just prevent the socket filter from being attached to any new sockets.

## Parameters

- `handle`: The sf_handle of the socket filter to unregister.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1433241-sflt_unregister)*