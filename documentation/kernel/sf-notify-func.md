# sf_notify_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef void (*sf_notify_func)(void *cookie, socket_t so, sflt_event_t event, void *param);
```

#### Discussion

sf_notify_func is called to notify the filter of various state changes and other events occuring on the socket.

## Parameters

- `cookie`: Cookie value specified when the filter attach was called.
- `so`: The socket the filter is attached to.
- `event`: The type of event that has occurred.
- `param`: Additional information about the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sf_notify_func)*