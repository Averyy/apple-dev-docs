# vfs_context_proc

**Framework**: Kernel  
**Kind**: func

Get the BSD process structure associated with a vfs_context_t.

**Availability**:
- macOS 10.4+

## Declaration

```swift
proc_t vfs_context_proc(vfs_context_t ctx);
```

#### Return_value

Process if available, NULL otherwise.

## Parameters

- `ctx`: Context whose associated process to find.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562390-vfs_context_proc)*