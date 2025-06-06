# sflt_attach

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

## Declaration

```swift
errno_t sflt_attach(socket_t socket, sflt_handle handle);
```

#### Return_value

0 on success otherwise the errno error.

#### Discussion

Attaches a socket filter to the specified socket. A filter must be registered before it can be attached.

## Parameters

- `socket`: The socket the filter should be attached to.
- `handle`: The handle of the registered filter to be attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1433214-sflt_attach)*