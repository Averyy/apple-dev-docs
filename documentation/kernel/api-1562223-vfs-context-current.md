# vfs_context_current

**Framework**: Kernel  
**Kind**: func

Get the vfs_context for the current thread, or the kernel context if there is no context for current thread.

**Availability**:
- macOS 10.5+

## Declaration

```swift
vfs_context_t vfs_context_current(void);
```

#### Return_value

Context for current thread, or kernel context if thread context is unavailable.

#### Discussion

Kexts should not use this function--it is preferred to use vfs_context_create(NULL) and vfs_context_rele(), which ensure proper reference counting of underlying structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562223-vfs_context_current)*