# vfs_context_pid

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Get the process id of the BSD process associated with a vfs_context_t.

**Availability**:
- macOS 10.4+

## Declaration

```c
int vfs_context_pid(vfs_context_t ctx);
```

#### Return Value

Process id.

## Parameters

- `ctx`: Context whose associated process to find.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562461-vfs_context_pid)*