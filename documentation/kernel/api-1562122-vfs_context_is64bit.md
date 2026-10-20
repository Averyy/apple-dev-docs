# vfs_context_is64bit

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Determine if a vfs_context_t corresponds to a 64-bit user process.

**Availability**:
- macOS 10.4+

## Declaration

```c
int vfs_context_is64bit(vfs_context_t ctx);
```

#### Return Value

Nonzero if context is of 64-bit process, 0 otherwise.

## Parameters

- `ctx`: Context to examine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562122-vfs_context_is64bit)*