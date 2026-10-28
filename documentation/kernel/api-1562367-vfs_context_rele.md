# vfs_context_rele

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Release references on components of a context and deallocate it.

**Availability**:
- macOS 10.4+

## Declaration

```c
int vfs_context_rele(vfs_context_t ctx);
```

## Return Value

Always 0.

## Discussion

A context should not be referenced after vfs_context_rele has been called.

## Parameters

- `ctx`: Context to release.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562367-vfs_context_rele)*