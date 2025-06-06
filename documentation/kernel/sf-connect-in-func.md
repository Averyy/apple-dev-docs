# sf_connect_in_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*sf_connect_in_func)(void *cookie, socket_t so, const struct sockaddr *from);
```

#### Return_value

Return: 0 - The caller will continue with normal processing of the connection. Anything Else - The caller will rejecting the incoming connection.

#### Discussion

sf_connect_in_func is called to filter inbound connections. A protocol will call this before accepting an incoming connection and placing it on the queue of completed connections. Warning: This filter is on the data path. Do not spend excesive time. Do not wait for data on another socket.

## Parameters

- `cookie`: Cookie value specified when the filter attach was called.
- `so`: The socket the filter is attached to.
- `from`: The address the incoming connection is from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sf_connect_in_func)*