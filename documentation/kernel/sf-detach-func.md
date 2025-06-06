# sf_detach_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef void (*sf_detach_func)(void *cookie, socket_t so);
```

#### Return_value

If you return a non-zero value, your filter will not be attached to this socket.

#### Discussion

sf_detach_func is called to notify the filter it has been detached from a socket. If the filter allocated any memory for this attachment, it should be freed. This function will be called when the socket is disposed of.

## Parameters

- `cookie`: Cookie value specified when the filter attach was called.
- `so`: The socket the filter is attached to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sf_detach_func)*