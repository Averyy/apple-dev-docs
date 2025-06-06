# vfs_context_create

**Framework**: Kernel  
**Kind**: func

Create a new vfs_context_t with appropriate references held.

**Availability**:
- macOS 10.4+

## Declaration

```swift
vfs_context_t vfs_context_create(vfs_context_t ctx);
```

#### Return_value

The new context, or NULL in the event of failure.

#### Discussion

The context must be released with vfs_context_rele() when no longer in use.

## Parameters

- `ctx`: Context to copy, or NULL to use information from running thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562360-vfs_context_create)*