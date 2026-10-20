# vfs_setextendedsecurity

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Mark a filesystem as supporting security controls beyond POSIX permissions.

**Availability**:
- macOS 10.4+

## Declaration

```c
void vfs_setextendedsecurity(mount_t mp);
```

#### Return Value

void.

#### Discussion

Specific controls include ACLs, file owner UUIDs, and group UUIDs.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523360-vfs_setextendedsecurity)*