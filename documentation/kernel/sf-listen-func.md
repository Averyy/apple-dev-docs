# sf_listen_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*sf_listen_func)(void *cookie, socket_t so);
```

#### Return_value

Return: 0 - The caller will continue with normal processing of listen. EJUSTRETURN - The caller will return with a value of 0 (no error) from that point without further processing the listen command. The protocol will not see the call. Anything Else - The caller will stop processing and return this error.

#### Discussion

sf_listen_func is called before performing listen on a socket.

## Parameters

- `cookie`: Cookie value specified when the filter attach was called.
- `so`: The socket the filter is attached to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sf_listen_func)*