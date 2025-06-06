# sf_accept_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.5+

## Declaration

```swift
typedef errno_t (*sf_accept_func)(void *cookie, socket_t so_listen, socket_t so, const struct sockaddr *local, const struct sockaddr *remote);
```

#### Return_value

Return: 0 - The caller will continue with normal processing of accept. EJUSTRETURN - The to be accepted socket will be disconnected prior to being returned to the caller of accept. No further control or data operations on the socket will be allowed. This is the recommended return value as it has the least amount of impact, especially to applications which don't check the error value returned by accept. Anything Else - The to be accepted socket will be closed and the error will be returned to the caller of accept. Note that socket filter developers are advised to exercise caution when returning non-zero values to the caller, since some applications don't check the error value returned by accept and therefore risk breakage.

#### Discussion

sf_accept_func is called after a socket is dequeued off the completed (incoming) connection list and before the file descriptor is associated with it. A filter can utilize this callback to intercept the accepted socket in order to examine it, prior to returning the socket to the caller of accept. Such a filter may also choose to discard the accepted socket if it wishes to do so.

## Parameters

- `cookie`: Cookie value specified when the filter attach was called.
- `so_listen`: The listening socket.
- `so`: The socket that is about to be accepted.
- `local`: The local address of the about to be accepted socket.
- `remote`: The remote address of the about to be accepted socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sf_accept_func)*