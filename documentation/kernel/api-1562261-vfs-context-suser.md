# vfs_context_suser

**Framework**: Kernel  
**Kind**: func

Determine if a vfs_context_t corresponds to the superuser.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vfs_context_suser(vfs_context_t ctx);
```

#### Return_value

Nonzero if context belongs to superuser, 0 otherwise.

## Parameters

- `ctx`: Context to examine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562261-vfs_context_suser)*