# vfs_context_ucred

**Framework**: Kernel  
**Kind**: func

Get the credential associated with a vfs_context_t.

**Availability**:
- macOS 10.4+

## Declaration

```swift
kauth_cred_t vfs_context_ucred(vfs_context_t ctx);
```

#### Return_value

Process if available, NULL otherwise.

#### Discussion

Succeeds if and only if the context has a thread, the thread has a task, and the task has a BSD proc.

## Parameters

- `ctx`: Context whose associated process to find.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562308-vfs_context_ucred)*