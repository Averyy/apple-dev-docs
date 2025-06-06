# sflt_detach

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

## Declaration

```swift
errno_t sflt_detach(socket_t socket, sflt_handle handle);
```

#### Return_value

0 on success otherwise the errno error.

#### Discussion

Detaches a socket filter from a specified socket.

## Parameters

- `socket`: The socket the filter should be detached from.
- `handle`: The handle of the registered filter to be detached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1433247-sflt_detach)*