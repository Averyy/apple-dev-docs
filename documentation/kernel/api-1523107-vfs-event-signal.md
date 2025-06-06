# vfs_event_signal

**Framework**: Kernel  
**Kind**: func

Post a kqueue-style event on a filesystem (EVFILT_FS).

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_event_signal(fsid_t *fsid, u_int32_t event, intptr_t data);
```

#### Return_value

void.

## Parameters

- `fsid`: Unused.
- `event`: Events to post.
- `data`: Unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523107-vfs_event_signal)*