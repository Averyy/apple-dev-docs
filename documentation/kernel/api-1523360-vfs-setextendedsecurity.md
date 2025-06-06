# vfs_setextendedsecurity

**Framework**: Kernel  
**Kind**: func

Mark a filesystem as supporting security controls beyond POSIX permissions.

**Availability**:
- macOS 10.4+

## Declaration

```swift
void vfs_setextendedsecurity(mount_t mp);
```

#### Return_value

void.

#### Discussion

Specific controls include ACLs, file owner UUIDs, and group UUIDs.

## Parameters

- `mp`: Mount to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1523360-vfs_setextendedsecurity)*