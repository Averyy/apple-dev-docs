# sf_data_in_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*sf_data_in_func)(void *cookie, socket_t so, const struct sockaddr *from, mbuf_t *data, mbuf_t *control, sflt_data_flag_t flags);
```

#### Return_value

Return: 0 - The caller will continue with normal processing of the data. EJUSTRETURN - The caller will stop processing the data, the data will not be freed. Anything Else - The caller will free the data and stop processing.

#### Discussion

sf_data_in_func is called to filter incoming data. If your filter intercepts data for later reinjection, it must queue all incoming data to preserve the order of the data. Use sock_inject_data_in to later reinject this data if you return EJUSTRETURN. Warning: This filter is on the data path. Do not spend excesive time. Do not wait for data on another socket.

## Parameters

- `cookie`: Cookie value specified when the filter attach was called.
- `so`: The socket the filter is attached to.
- `from`: The addres the data is from, may be NULL if the socket is connected.
- `data`: The data being received. Control data may appear in the mbuf chain, be sure to check the mbuf types to find control data.
- `control`: Control data being passed separately from the data.
- `flags`: Flags to indicate if this is out of band data or a record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sf_data_in_func)*